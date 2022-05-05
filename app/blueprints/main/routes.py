from flask import render_template, current_app as app

@app.route('/')
def home():
    # raise Exception("This is a general exception")
    return render_template('main/home.html')


@app.route('/about')
def about():
    return render_template('main/about.html')


@app.route('/contact')
def contact():
    return render_template('main/contact.html')

@app.route('/register')
def register():
    return render_template('main/register.html')