from flask import Flask, render_template, flash, jsonify, request
from blueprints.main import main
from blueprints.contact import contact
from blueprints.auth import auth
from blueprints.api import api
from blueprints.blog import blog

app = Flask(__name__)       # Create a flask app instance
app.secret_key = 'my-secret-key-1234'

app.register_blueprint(main)
app.register_blueprint(contact)
app.register_blueprint(auth)
app.register_blueprint(api)
app.register_blueprint(blog)

@app.errorhandler(404)  
def page_not_found(error):
  if request.path.startswith('/api'):
    return jsonify({'error': 'Endpoint not found'}), 404
  flash('Oops! That page doesn’t exist.', 'error')
  return render_template('404.html'), 404

if __name__ ==  '__main__':
  app.run(debug=True)       # Run app in debug mode