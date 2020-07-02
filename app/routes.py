from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')

def hello():
    title = 'Food-site-title'
    return render_template('index.html', title = title, active='main'.lower())

