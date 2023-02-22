import flask
from flask import Flask, url_for, render_template, request
from faker import Faker


app = Flask(__name__)
fake = Faker()

@app.route('/requirements/')
def open_file():
    with open('requirements.txt', 'r') as file:
        text = file.read().splitlines()
    return text


@app.route('/generate-users/')
def generate_users():
    user_data = []
    count = int(request.args.get('count', default=100))
    return render_template('users.html', count= count)

