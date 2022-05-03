from app import app

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "Contact"