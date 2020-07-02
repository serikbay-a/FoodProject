from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')

def hello():
    title = 'Food-site-title'
    return render_template('index.html', title = title, active='catalog'.lower())

@app.route('/select/')
def select():
    title = 'Рецепт по ингредиентам'
    return render_template('select.html', title = title, active='select'.lower())