from flaskapp import app
from flask import make_response
from flaskapp.models import db, AriaKaroFactorial

from flask import (
    flash, render_template, request, abort, url_for, session, redirect
)

import os 


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    message = f'welcome back {session.get("username")}'
    if session.get('username'):

        return render_template('index.html', message=message)

    else:

        return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        default_user = 'AriaKaro'
        server_password = '1122334455'
        
        response = make_response(render_template('index.html'))
        session['username'] = username
        session.permanent = True
        
        
        if username != default_user or password != server_password:
            a = "Username or Password wrong !"
                     
            return render_template('form.html',a = a)
        
        else:

            return render_template('index.html')

@app.route('/compute', methods=['POST', 'GET'])
def compute():
 
    if request.method == 'POST':


        salary_price = request.form['salary_price']
        contract_price = request.form['contract_price']
        taxation = float(request.form['taxation'])
        taxation_c = float(request.form['taxation_c'])
        value_added = float(request.form['value_added'])
        insurance = float(request.form['insurance'])



        if salary_price and contract_price != '':

            finale_price = float(salary_price) + float(contract_price)

            c = (finale_price * taxation) *  taxation_c
            d = finale_price * value_added
            e = finale_price * insurance
            factor_price = c + d + e + finale_price

        else:

            a = "please fill the form first :)"
            return render_template('index.html', a = a)

        return render_template('result.html',
                  
                               finale_price=finale_price, 
                               factor_price=factor_price 
                               )

    
@app.route('/edit/<int:factor_id>', methods=['POST', 'GET'])
def edit(factor_id):

    factor = AriaKaroFactorial.query.get_or_404(factor_id)

    if request.method == 'POST':

        taxation = float(request.form['taxation'])
        taxation_c = float(request.form['taxation_c'])
        value_added = float(request.form['value_added'])
        insurance = float(request.form['insurance'])

        factor.taxation = taxation
        factor.taxation_c = taxation_c
        factor.value_added = value_added
        factor.insurance = insurance

        db.session.add(factor)
        db.session.commit()

        return redirect(url_for('login'))

    
    return render_template('edit.html', factor=factor)

