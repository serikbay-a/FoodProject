from app import app
from flask import render_template, redirect, url_for, request
from app.forms import MyForm, MultiCheckboxField, SimpleForm
import sys
import codecs
import os
from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingridients = db.Column(db.String(2000), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    url_img = db.Column(db.String(1000))
    category = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<{} name: {} ingridients: {} url: {} url_img: {} category: {} time: {}>'.format(self.id,self.name,self.ingridients,self.url,self.url_img,self.category,self.time)

@app.route('/')
@app.route('/index')
@app.route('/catalog')
def catalog():
    title = 'имя-сайта'
    cards = []
    r = Recipe
    q = r.query.all()
    for i in q:
        url = i.url
        name = i.name
        url_img = i.url_img
        category = i.category
        ingridients = i.ingridients
        time = 0
        cards.append({"name":name, "url":url, 'url_img':url_img, 'category':category,'ingridients':ingridients, 'time': time})

    return render_template('catalog.html', title = title, active='catalog'.lower(), cards = cards)
    

@app.route('/select', methods=['GET', 'POST'])
def select():
    cards = []
    form = SimpleForm()
    title = 'Рецепт по ингредиентам'
    if form.validate_on_submit():
        #print(form.cb.data)
        n=0
        cb_data = form.cb1.data + form.cb2.data + form.cb3.data
        #print(cb_data)

        r = Recipe
        q = r.query.all()

        for i in q:
            #print(i.ingridients)
            listt = cb_data #sel ingr
            ilistt = i.ingridients.split(',') #rec ingr
            good = True
            for j in ilistt:
                j=j.strip(' ')
                j=j.strip()
                if j!='' and j not in listt:
                    good = False
                    pass
            if good:

                url = i.url
                name = i.name
                url_img = i.url_img
                category = i.category
                ingridients = i.ingridients
                time = 0
                cards.append({"name":name, "url":url, 'url_img':url_img, 'category':category,'ingridients':ingridients, 'time': time})
                
                n+=1
                #print(i)
        #print(n)
        #print(cards)
        return render_template('catalog.html', title = title, active='catalog'.lower(), cards = cards)
        #return render_template("success.html", data=cb_data)
    return render_template('select.html', title = title, active='select'.lower(), form=form)

@app.route('/donate')
def donate():
    title = 'Поддержать проект'
    return render_template('donate.html', title = title, active='donate'.lower())

@app.route('/add', methods=('GET', 'POST'))
def add():
    form = MyForm()
    if form.validate_on_submit():
        name = request.form['name']
        ingridients = request.form['ingridients']
        url = request.form['url']
        url_img = request.form['url_img']
        category = request.form['category']
        time = request.form['time']

        recipe = Recipe(
                        name=name,
                        ingridients=ingridients,
                        url=url,
                        url_img=url_img,
                        category=category,
                        time=time
                        )
        print(recipe)

        
        db.session.add(recipe)
        db.session.commit()
        print('Sucsess!!!')    
        
    return render_template('add.html', active='donate'.lower(), form = form)