from flask import Blueprint, render_template, session, redirect, flash, request, url_for
from app import dict

auth_bp = Blueprint('auth', __name__)



@auth_bp.route('/', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == dict.USER_CREDENTIALS['username'] and password == dict.USER_CREDENTIALS['password']:
            session['user'] = username
            flash("Login Successful!")
        else:
            flash('Invalid credentials!')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out succefully")
    return redirect(url_for('auth.login'))

