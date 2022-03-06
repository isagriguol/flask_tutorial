from flask import render_template, url_for, flash, redirect, request
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# as classes de uma estrutura de base de dados se chamam MODELS
# os models podem ser no mesmo código ou em arquivos separados

@app.route('/')
def index():
    return render_template('layout.html')

# @app.route('/')
# def index():
#    return render_template('flash_index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
                    error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('layout'))
            # return redirect(url_for('success'))
    return render_template('login.html', error=error)
