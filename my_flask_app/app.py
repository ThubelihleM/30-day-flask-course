# app.py
from flask import Flask

app = Flask(__name__)       # Create a flask app instance

@app.route('/')             # Route for home page
def home():
  return 'Hello, Flask!'    # Return text to browser

@app.route('/about')
def about():
  return 'This is the About Page'

@app.route('/user/<name>')
def user(name):
  return f'Hello {name}!'

@app.route('/contact')
def contact():
  return 'Contact Us at support@example.com'

@app.route('/greet/<username>')
def greet(username):
  return f'Welcome, {username}!'

if __name__ ==  '__main__':
  app.run(debug=True)       # Run app in debug mode