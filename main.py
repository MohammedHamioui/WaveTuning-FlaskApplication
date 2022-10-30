import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class car(db.Model):
    id = db.Column('car_id', db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(200))
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.String(50))


def __init__(self, firstName, lastName, email, make, model, year):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.make = make
    self.model = model
    self.year = year


@app.route('/')
def home():
    imageList = os.listdir('static/images/popularbrandlogos')
    imageList = ['images/popularbrandlogos/' + image for image in imageList]
    return render_template('index.html', imageList=imageList, car=car.query.all())


@app.route('/appointment/', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        if not request.form['firstName'] or not request.form['lastName'] or not request.form['email'] or not request.form['make'] or not request.form['model'] or not request.form['year']:
            flash('Please enter all the fields', 'error')
        else:
            cars = car( firstName= request.form['firstName'],lastName=  request.form['lastName'], email=request.form['email'], make=request.form['make'], model=request.form['model'], year=request.form['year'])
            db.session.add(cars)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('Confirm'))
    return render_template('appointment.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/services/')
def services():
    return render_template('services.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/products/')
def products():
    return render_template('products.html')


@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')


@app.route('/WhatIsChiptuning/')
def WhatIsChiptuning():
    return render_template('WhatIsChiptuning.html')


@app.route('/PopsAndBangs/')
def PopsAndBangs():
    return render_template('PopsAndBangs.html')


@app.route('/SupportedBrands/')
def SupportedBrands():
    brands = os.listdir('static/images/carbrands')
    brands = ['images/carbrands/' + image for image in brands]
    return render_template('SupportedBrands.html', brands=brands)


@app.route('/DTE/')
def DTE():
    return render_template('DTE.html')


@app.route('/PowerMeasurement/')
def PowerMeasurement():
    return render_template('PowerMeasurement.html')


@app.route('/Maxhaust/')
def Maxhaust():
    return render_template('Maxhaust.html')


@app.route('/ECOtuning/')
def ECOtuning():
    return render_template('ECOtuning.html')


@app.route('/S1orS2/')
def S1orS2():
    return render_template('S1orS2.html')

@app.route('/Confirm/')
def Confirm():
    return render_template('Confirm.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
