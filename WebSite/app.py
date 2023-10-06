from flask import Flask, render_template, request , redirect,url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('welcome.html')

@app.route("/login")
def login():
    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')
        

