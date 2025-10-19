# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages

app = Flask(__name__)       # Create a flask app instance
app.secret_key = 'my-secret-key-1234'

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    if not name or not message or not email or '@' not in email:
      flash('Please fill out all fields.', 'error')
      return render_template('contact.html')
    flash(f'Thanks for contacting us, {name}! Your message: {message}', 'success')
    return redirect(url_for('contact_success'))
  return render_template('contact.html', error=None)

@app.route('/contact/success')
def contact_success():
  return render_template('contact_success.html')

@app.route('/echo', methods=['GET', 'POST'])
def echo():
  if request.method == 'POST':
    my_input = request.form['theInput']
    
    if not my_input:
      return render_template('echo.html', error='Input should be unempty.')
    return redirect(url_for('echo_success', my_input=my_input))
  
  return render_template('echo.html')

@app.route('/echo/success')
def echo_success():
  my_input = request.args.get('my_input')
  return render_template('echo_success.html', my_input=my_input)

@app.errorhandler(404)  
def page_not_found(error):
  flash('Oops! That page doesn’t exist.', 'error')
  return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
  flash('Internal Server Error.', 'error')
  return render_template('500.html'), 500

if __name__ ==  '__main__':
  app.run(debug=True)       # Run app in debug mode