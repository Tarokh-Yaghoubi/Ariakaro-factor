from flaskapp import app
from flask import make_response
from flaskapp.models import db, AriaKaroFactorial
from flask_login import login_required

from flask import (
    flash, render_template, request, abort, url_for, session, redirect
)

import os 


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    global factor
    
    message = f'welcome back {session.get("username")}'
    if session.get('username'):
        factor = AriaKaroFactorial.query.get(1)
        return render_template('index.html', factor=factor, message=message)

    else:

        return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():

    global factor
    factor = AriaKaroFactorial.query.get(1)
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        default_user = 'AriaKaro'
        server_password = '1'
        
        response = make_response(render_template('index.html', factor=factor))
        session['username'] = username
        session.permanent = True
        
        
        if username != default_user or password != server_password:
            a = "Username or Password wrong !"
                     
            return render_template('form.html',a = a)
        
        else:
            return response


@app.route('/compute', methods=['POST', 'GET'])
def compute():


    
    if request.method == 'POST':

        try:

            salary_price = float(request.form.get('salary_price'))
            contract_price = float(request.form.get('contract_price'))
            taxation = float(request.form.get('taxation'))

            taxation_c = float(request.form.get('taxation_c'))
            value_added = float(request.form.get('value_added'))
            insurance = float(request.form.get('insurance'))

        except ValueError:

            if salary_price == '' or float(0):

                salary_price = float(0)

            elif contract_price == '' or float(0):

                contract_price = float(0)
            
            elif taxation == '' or float(0):

                taxation = float(0)

            elif taxation_c == '' or float(0):

                taxation_c = float(0)

            if value_added == '' or float(0):

                value_added = float(0)

            if insurance == '' or float(0):

                insurance = float(0)
        

        if salary_price and contract_price != '':

            finale_price = float(salary_price) + float(contract_price)



            c = (finale_price * taxation) *  taxation_c
            d = finale_price * value_added
            e = finale_price * insurance
            factor_price = c + d + e + finale_price

            c = float(c)
            d = float(d)
            e = float(e)
            factor_price = float(factor_price)
        else:

            a = "please fill the form first :)"
            return render_template('index.html', a = a)

        return render_template('result.html', finale_price=finale_price, factor_price=factor_price, c=c, d=d, e=e)

    
@app.route('/edit/<float:factor_id>', methods=['POST', 'GET'])
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


@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html'), 404

@app.errorhandler(500)
def error_503(error):
    return render_template('error_500.html'), 500