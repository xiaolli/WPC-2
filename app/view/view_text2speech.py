from flask import Flask,request,render_template
from app.controller.text2speech import test2speech
from app import app
import os

@app.route('/helloflask')
def index():
    return "hello flask"

@app.route('/text2speech')
def text2speech():
    return render_template('text2speech_text.html')

@app.route('/dotext2speech',methods=['GET','POST'])
def dotext2speech():
    print(11111)
    #if request.method == 'GET':
    #text = request.args.get('message')

    if request.method == 'POST':
        text = request.form['message']
        print (text)
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/')

        filename ='text2speech.wav'

        test2speech(text=text,filename=path + filename)


        return render_template('text2speech_play.html',filename=filename)