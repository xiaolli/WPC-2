from app import app
import config
from werkzeug.utils import secure_filename
from flask import request,send_from_directory,url_for,render_template
import os
from app.controller.upload import save_file,query_file

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = config.DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH


#检查上传文件合法性
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in config.ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    return send_from_directory(app.config['DOWNLOAD_FOLDER'],filename)

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        userSN= request.form['usersn']
        if file and allowed_file(file.filename):
            filename =secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            #file_url = url_for('uploaded_file', filename=filename)

            save_file(userSN,img_filename)
            ##save_file(userSN,file)

            img=query_file(userSN)

            down_filename=os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
            with open(down_filename,'wb') as downimage:
                downimage.write(img["user_IMG"])

            file_url = url_for('uploaded_file', filename=filename)

            #pipe = open(os.path.join(app.config['DOWNLOAD_FOLDER'], filename),'wb')

            #pipe.write(img["user_IMG"])

            #print(img["user_IMG"])
            #img.write(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            #file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #mongo.save_file(filename,request.files['file'])

            #file_url = url_for('uploaded_file',filename=filename)
            return render_template('VisualRecognition.html') + img["userSN"] +'<br><img src=' + file_url + '>'
            #return render_template('VisualRecognition.html') + userSN +'<br><img src=' + file_url + '>'

    return render_template('VisualRecognition.html')


