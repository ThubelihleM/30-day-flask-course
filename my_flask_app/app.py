# app.py
from flask import Flask, render_template

app = Flask(__name__)       # Create a flask app instance

@app.route('/')             # Route for home page
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/user/<name>')
def user(name):
  user_info = {'name': name, 'age': 25}
  return render_template('user.html', user_info=user_info)

@app.route('/fruits')
def fruits():
  fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
  return render_template('fruits.html', fruits=fruits_list)

@app.route('/hobbies')
def hobbies():
  hobbies = ['Reading', 'Gaming', 'Coding']
  return render_template('hobbies.html', hobbies=hobbies)

if __name__ ==  '__main__':
  app.run(debug=True)       # Run app in debug mode