from flask import Flask, render_template, request , redirect

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def index():
    return render_template('welcome.html')

@app.route("/login")
def login():
    return render_template('login.html')



@app.route("/signup")
def signup():
    return render_template('register.html')

