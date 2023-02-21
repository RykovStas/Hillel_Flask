from flask import Flask

app = Flask(__name__)


@app.route('/requirements/')
def open_file():
    text =''
    with open('requirements.txt') as file:
        text = file.read().splitlines()
        return text

