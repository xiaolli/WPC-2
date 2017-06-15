import os

#上传文件要储存的目录
#upload_path = os.path.split(os.path.realpath(__file__))[0] + '/app/static/tmp/uploadfile'
upload_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'tmp/uploadfiles')
download_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'tmp/downloadfiles')

#print(upload_path)
#print(os.path.dirname(__file__))
UPLOAD_FOLDER = upload_path
DOWNLOAD_FOLDER = download_path
#允许 上传的文件扩展名的集合
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#ALLOWED_EXTENSIONS = set(['wav', 'flac'])

#限制文件大小
MAX_CONTENT_LENGTH = 16 * 1024 * 1024