from flaskapp import app

from flask import make_response

from flask import (
    flash, render_template, request, abort, url_for, session, redirect
)

import os 


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        
        default_user = 'AriaKaro'
        server_password = '1122334455'
        
        response = make_response(render_template('admin.html'))
        session['_username'] = username
        session.permanent = True
        
        
        if username != default_user and password != server_password:
            a = "Username or Password wrong !"
             #'<script>alert("");</script>'
        
            return render_template('form.html',a=a)
        
        elif session.get('username'):
            
            return render_template('admin.html')
        
        else:
            
            return render_template('form.html', a=a)