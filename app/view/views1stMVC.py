from app import app
from flask import render_template,request

@app.route('/',methods=['GET','POST'] )
def index():

    if request.method == 'POST':
        username = request.form.get('username')
        return "Hello  " + username
    else:
        return render_template('FirstMVC.html')