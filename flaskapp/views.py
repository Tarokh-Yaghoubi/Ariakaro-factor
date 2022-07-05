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
            salary_price = float(request.form.get('salary_price') if request.form.get('salary_price')!='' else 0)
            contract_price = float(request.form.get('contract_price')  if request.form.get('contract_price')!='' else 0)
            taxation = float(request.form.get('taxation') if request.form.get('taxation')!='' else 0)

            taxation_c = float( request.form.get('taxation_c')if request.form.get('taxation_c')!='' else 0)
            value_added = float(request.form.get('value_added') if request.form.get('value_added')!='' else 0)
            insurance = float(request.form.get('insurance') if request.form.get('insurance')!='' else 0)

            final_price = salary_price+ contract_price
            c = (final_price * taxation) * taxation_c
            d = final_price * value_added
            e = final_price * insurance
            factor_price = c + d + e + final_price
            #a = "please fill the form first :)"
            #return render_template('index.html', a = a)
            return render_template('result.html', finale_price=int(final_price), factor_price=int(factor_price), c=int(c), d=int(d), e=int(e))

    
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