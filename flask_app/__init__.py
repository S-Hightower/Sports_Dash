from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'