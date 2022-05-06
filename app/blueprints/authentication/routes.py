#  route for user authentication "signup"

from flask import current_app as app, render_template

@app.route('/register')
def register():
    return render_template('main/register.html')
