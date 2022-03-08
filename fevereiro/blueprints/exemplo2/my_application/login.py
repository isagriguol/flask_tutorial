from flask import Blueprint, flash, redirect, render_template, request, url_for

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        flash('You were successfully logged in')
        return redirect(url_for('index'))
        #return redirect(url_for('success'))
    return render_template('login.html', error=error)