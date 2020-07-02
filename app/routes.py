from app import app
from flask import render_template, redirect, url_for


@app.route('/')
@app.route('/index')
@app.route('/catalog')
def catalog():
    title = 'имя-сайта'
    return render_template('catalog.html', title = title, active='catalog'.lower())
    

@app.route('/select/')
def select():
    title = 'Рецепт по ингредиентам'
    return render_template('select.html', title = title, active='select'.lower())


@app.route('/donate/')
def donate():
    title = 'Поддержать проект'
    return render_template('donate.html', title = title, active='donate'.lower())