from flask import render_template, current_app as app, request, redirect, url_for, flash
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User



@app.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        print(current_user)
    # raise Exception("This is a general exception")
    if request.method == 'POST':
        print("="*60)
        print("THIS WORKS")
        print("="*60)
        return redirect(url_for('home'))
    return render_template('main/home.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        form_data = request.form

        user = User.query.get(current_user.get_id())
        user.first_name = form_data.get('first_name')
        user.last_name = form_data.get('last_name')
        user.email = form_data.get('email')
        
        if len(form_data.get('password')) == 0:
            pass
        elif form_data.get('password') == form_data.get('confirm_password'):
            user.generate_password(form_data.get('password'))
        else:
            flash('There was an error updating your password', 'danger')
            return redirect(url_for('profile'))

        db.session.commit()

        flash('You have updated your information', 'primary')
        return redirect(url_for('profile'))
    return render_template('main/profile.html')


@app.route('/contact')
def contact():
    return render_template('main/contact.html')

