# controller handles routing and rendering templates

from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
# from flask_app.models.model_data import Data

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')