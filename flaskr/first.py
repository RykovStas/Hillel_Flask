import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

import functools
import flask
from flask import Flask, url_for, render_template, request
from faker import Faker
import pandas as pd
import requests

fake = Faker()



bp = Blueprint('first', __name__, url_prefix='/first')


@bp.route('/requirements/')
def open_file():
    with open('requirements.txt', 'r') as file:
        text = file.read().splitlines()
    return text


@bp.route('/generate-users/')
def generate_users():
    users = []
    count = request.args.get('count', default=100, type=int)
    for _ in range(count):
        name = fake.name()
        email = fake.email()
        users.append({"name": name, "email": email})
    return render_template('users.html', users=users)


@bp.route('/mean/')
def mean():
    dataset = pd.read_csv('hw.csv')
    average = dataset.mean()
    return f"Avarage height {round(average.values[1] * 2.54)}sm, Avarage weight {round(average.values[2] / 2.2)}kg"


@bp.route('/space/')
def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts_count = r.json()['number']
    response = flask.jsonify(count=astronauts_count)
    return response