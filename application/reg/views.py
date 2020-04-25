import sqlite3

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.reg.forms import RegisterForm


@app.route("/reg/register", methods=["GET", "POST"])
def reg_register():

    if request.method == "GET":
        return render_template("reg/registerform.html", form = RegisterForm())

    if request.method == "POST":
        form = RegisterForm(request.form)
        username  = form.username.data
        name = form.name.data
        password = form.password.data
        confirm = form.confirm.data

        users = User.query.filter_by(username=username).first()

        if users:
            return render_template("reg/registerform.html", form = form, error = "Username taken, pick a new one!")

        if not password == confirm:
            return render_template("reg/registerform.html", form = form, error = "Passwords must match!")

        if not users and password == confirm:
            u = User(name, username, password)
            db.session().add(u)
            db.session().commit()
            return redirect(url_for("artikkelit_index"))
        