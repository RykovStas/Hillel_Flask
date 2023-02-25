import os
import flask
from flask import Flask, url_for, render_template, request
from faker import Faker
import pandas as pd
import requests


fake = Faker()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/requirements/')
    def open_file():
        with open('requirements.txt', 'r') as file:
            text = file.read().splitlines()
        return text

    @app.route('/generate-users/')
    def generate_users():
        users = []
        count = request.args.get('count', default=100, type=int)
        for _ in range(count):
            name = fake.name()
            email = fake.email()
            users.append({"name": name, "email": email})
        return render_template('users.html', users=users)

    @app.route('/mean/')
    def mean():
        dataset = pd.read_csv('hw.csv')
        average = dataset.mean()
        return f"Avarage height {round(average.values[1] * 2.54)}sm, Avarage weight {round(average.values[2] / 2.2)}kg"

    @app.route('/space/')
    def get_astronauts():
        r = requests.get('http://api.open-notify.org/astros.json')
        astronauts_count = r.json()['number']
        response = flask.jsonify(count=astronauts_count)
        return response

    from . import db
    db.init_app(app)

    return app