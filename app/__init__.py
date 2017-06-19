from flask import Flask

app = Flask(__name__)

#app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

from app.view import views

####from app.view import view_text2speech

