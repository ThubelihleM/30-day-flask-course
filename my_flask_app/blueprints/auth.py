from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth')

@auth.route('/signup')
def sign_up():
  return render_template('auth/signup.html')