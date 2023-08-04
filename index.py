from pywebio.platform.flask import *
from flask import Flask, render_template
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
import os

from teacher import create_exam
from student import take_exam

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024

def main():
    put_html('<h2>Welcome to the Exam Portal</h2>')
    choice = select("Select your role:", options=["Teacher", "Student"])
    
    if choice == "Teacher":
        create_exam()
    else:
        take_exam()

app.add_url_rule('/', 'webio_view', webio_view(main), methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
