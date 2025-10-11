from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Get form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    # Basic validation
    if not first_name or not last_name or not email or not password or not confirm_password:
        flash('Please fill in all required fields.', 'error')
        return redirect(url_for('contact'))
    
    if password != confirm_password:
        flash('Passwords do not match.', 'error')
        return redirect(url_for('contact'))
    
    if len(password) < 8:
        flash('Password must be at least 8 characters long.', 'error')
        return redirect(url_for('contact'))
    
    # Here you would typically save the form data to a database
    # For now, we'll just redirect to the thank you page
    flash('Thank you for your message! We will get back to you soon.', 'success')
    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)
