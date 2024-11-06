#!/usr/bin/env python3
"""simple flask app"""
from flask import render_template, Flask
from flask_babel import Babel
import typing

app = Flask(__name__)
babel = Babel()


@app.route('/')
def index_page() -> typing.Any:
    """renders index page"""
    return render_template('index.html')
