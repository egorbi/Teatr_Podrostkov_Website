from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')

def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up')
def sign_up():
    return '<p>Sign up</p>'

@auth.route('/afisha')
def afisha():
    return render_template("afisha.html")

@auth.route('/home')
def home():
    return render_template("home.html")