from app import app
from flask import render_template, redirect, url_for, request
from app.forms import MyForm
import sys
import codecs
import os
from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    recipe = db.Column(db.String(1000), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100))
    time = db.Column(db.String(255))

@app.route('/')
@app.route('/index')
@app.route('/catalog')
def catalog():
    title = 'имя-сайта'
    cards = [{'title':'Курочка с хреном', 'pic':'https://img1.russianfood.com/dycontent/images_upl/185/big_184766.jpg', 'url': '', 'recipe':['курочка', "хрен", "майонезик", "соус"]}]
    return render_template('catalog.html', title = title, active='catalog'.lower(), cards = cards)
    

@app.route('/select/')
def select():
    title = 'Рецепт по ингредиентам'
    return render_template('select.html', title = title, active='select'.lower())


@app.route('/donate/')
def donate():
    title = 'Поддержать проект'
    return render_template('donate.html', title = title, active='donate'.lower())

@app.route('/add/', methods=('GET', 'POST'))
def add():
    form = MyForm()
    if form.validate_on_submit():
        _, file_ext = os.path.splitext(form.file.data.filename)
        files_dir= os.path.join(os.getcwd(), 'files')
        fname=form.name.data+file_ext
        filename=os.path.join(files_dir, fname)
        if 'files' not in os.listdir(os.getcwd()):
            os.mkdir(files_dir)
        form.file.data.save(filename)

        name_of_dish = request.form['name_of_dish']
        ingridients = request.form['ingridients']
        url = request.form['url']
        category = request.form['category']
        time = request.form['time']

        recipe = Recipe(name=name_of_dish,recipe=ingridients,url=url,category=category,time=time)

        try: 
            db.session.add(recipe)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error!!!'
    return render_template('add.html', active='donate'.lower(), form = form)