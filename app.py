import flask
from flask import Flask, url_for, render_template, request
from faker import Faker
import pandas as pd


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


@app.route('/mean/')

def mean():
    dataset = pd.read_csv('hw.csv')
    average = dataset.mean()
    return f"Avarage height {round(average.values[1]*2.54)}sm, Avarage weight {round(average.values[2]/2.2)}kg"


