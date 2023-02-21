from flask import Flask

app = Flask(__name__)


@app.route('/requirements/')
def open_file():
    with open('requirements.txt', 'r') as file:
        text = file.read().splitlines()
    return text

