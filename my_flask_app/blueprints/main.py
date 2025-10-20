from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='main')

@main.route('/')
def home():
  return render_template('main/home.html')

@main.route('/about')
def about():
  return render_template('main/about.html')

@main.route('/fruits')
def fruits():
  fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
  return render_template('main/fruits.html', fruits=fruits_list)

@main.route('/user/<name>')
def user(name):
  return render_template('main/user.html', username=name)

