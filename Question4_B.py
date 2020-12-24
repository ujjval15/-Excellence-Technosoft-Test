from flask import Blueprint, render_template, url_for, request, redirect
from . import db


auth = Blueprint('app', __name__)

@app.route("/")
def home():
    return "My flask app"

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    address = request.form.get('address')
    password = request.form.get('password')

    new_user = User(email=email, name=name,address=address, password=password)
    db.session.add(new_user)
    db.session.commit()

    print(email,name,password)

    return redirect(url_for('auth.login'))

@ auth.route('/login')
def login():
    return render_template('login.html')


@ auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email,password)

@app.route("/updateaddress", methods=["POST"])
def update():
    newaddress = request.form.get("newtaddress")
    oldaddress = request.form.get("oldaddress")
    address = address.query.filter_by(title=oldaddress).first()
    address = newaddress
    db.session.commit()
    return redirect("")
