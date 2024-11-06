#!/usr/bin/env python3
"""simple flask app"""
from flask import render_template, Flask, request
from flask_babel import Babel
import typing


app = Flask(__name__)
app.config.from_object('config.Config')
babel = Babel(app)


@babel.localselector
def get_locale():
    """returns language locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_page() -> typing.Any:
    """renders index page"""
    return render_template('index.html')
