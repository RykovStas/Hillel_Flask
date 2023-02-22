# Hillel_Flask

> This is 3rd HomeWork

* Task 1
```python
import flask
from flask import Flask, url_for, render_template, request


app = Flask(__name__)


@app.route('/requirements/')
def open_file():
    with open('requirements.txt', 'r') as file:
        text = file.read().splitlines()
    return text
```
- [x] In this task, we open a file requirements.txt and read its contents


* Task 2
```python
from faker import Faker

fake = Faker()

@app.route('/generate-users/')
def generate_users():
    user_data = []
    count = int(request.args.get('count', default=100))
    return render_template('users.html', count= count)
```
- [x] In this task we randomly generate 100 users and mail. Also adding a get parameter

* Task 3
```python
import pandas as pd

@app.route('/mean/')
def mean():
    dataset = pd.read_csv('hw.csv')
    average = dataset.mean()
    return f"Avarage height {round(average.values[1]*2.54)}sm, Avarage weight {round(average.values[2]/2.2)}kg"
```
- [x] In this task, we read information from a file hw.csv and output the average height and average weight

* Task 4
```python
import requests
import flask

@app.route('/space/')
def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts_count = r.json()['number']
    response = flask.jsonify(count=astronauts_count)
    return response
```
- [x] In this task, we display the number of astronauts from the API source