from flask import Flask, render_template, flash
from blueprints.main import main
from blueprints.contact import contact
from blueprints.auth import auth

app = Flask(__name__)       # Create a flask app instance
app.secret_key = 'my-secret-key-1234'

app.register_blueprint(main)
app.register_blueprint(contact)
app.register_blueprint(auth)

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