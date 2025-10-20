from flask import Blueprint, render_template, request, redirect, url_for, flash

contact = Blueprint('contact', __name__, template_folder='contact')

@contact.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        if not name or not message:
            flash('Please fill out all fields.', 'error')
            return render_template('contact/contact.html')
        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact.contact_success', name=name, message=message))
    return render_template('contact/contact.html')

@contact.route('/contact/success')
def contact_success():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('contact/contact_success.html', name=name, message=message)