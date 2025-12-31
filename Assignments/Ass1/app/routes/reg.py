from flask import Blueprint, redirect, render_template, request, url_for
from app import dict

reg_bp = Blueprint('reg', __name__)

@reg_bp.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == "POST":

        dict.USER_CREDENTIALS['username1'] = request.form.get('username1')
        dict.USER_CREDENTIALS['password1'] = request.form.get('password1')

    return render_template('register.html')
        