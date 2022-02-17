from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_data import Data

@app.route('/')
def livescores():
    return render_template('test.html')