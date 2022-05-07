#  route for user authentication "signup"
from crypt import methods
from flask import current_app as app, render_template, request, redirect, url_for, flash
from .models import User
from app import db

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form
        
        if form_data.get('password') == form_data.get('confirm_password'):
            user = User(
                first_name=form_data.get('first_name'),
                last_name=form_data.get('last_name'),
                email=form_data.get('email_address'),
            )
            user.generate_password(form_data.get('password'))
            db.session.add(user)
            db.session.commit()

            flash('You have registered successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash("Your passwords don't match. Please try again.", "warning")
        return redirect(url_for('register'))
    
    return render_template('users/register.html')
