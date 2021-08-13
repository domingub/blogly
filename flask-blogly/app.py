"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def homepage():
    """Homepage"""

    return redirect("/users")

@app.route("/users")
def users():
        users = User.query.order_by(User.last_name, User.first_name).all()
        return render_template('userlist.html', users = users)

@app.route("/users/new", methods = {"GET"})
def add_user():
    return render_template('newuser.html')

@app.route("/users/<user_id>")
def profile_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user = user)

@app.route("/users/<user-id>/edit", methods = {"GET"})
def edit_user():
    return render_template('profile.html')

@app.route("//users/<user-id>/delete")