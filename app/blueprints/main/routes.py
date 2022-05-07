from flask import render_template, current_app as app, request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def home():
    # raise Exception("This is a general exception")
    if request.method == 'POST':
        print("="*60)
        print("THIS WORKS")
        print("="*60)
        return redirect(url_for('home'))
    return render_template('main/home.html')


@app.route('/about')
def about():
    return render_template('main/about.html')


@app.route('/contact')
def contact():
    return render_template('main/contact.html')

