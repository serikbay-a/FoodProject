from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')

def hello():
    text = 'Food-site-title'
    return render_template('index.html', title = text)

