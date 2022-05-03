from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('main/home.html')

@app.route('/about')
def about():
    return render_template('main/about.html')

@app.route('/contact')
def contact():
    return render_template('main/contact.html')