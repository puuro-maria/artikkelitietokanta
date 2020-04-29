from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
  
from application import app, LoginManager, login_required, db
from application.auth.models import User
from application.auth.forms import LoginForm

from application.artikkelit.models import Artikkeli

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/allusers", methods=["GET"])
@login_required(role="ADMIN")
def auth_list_all_users():

    return render_template("allusers.html", accounts = db.session.query(User.id, User.username, User.name, sa.func.coalesce(sa.func.count(Artikkeli.id), 0).label('articles')).outerjoin(Artikkeli, Artikkeli.account_id == User.id).group_by(User.id))


@app.route("/manageaccount/<account_id>/", methods=["GET"])
@login_required
def auth_manage_account(account_id):

    return render_template("manageaccount.html", accounts = db.session.query(User.id, User.username, User.name, (sa.func.coalesce(sa.func.count(Artikkeli.id), 0)).label('articles')).join(Artikkeli, Artikkeli.account_id == User.id).group_by(User.id).filter_by(account_id = current_user.id))

@app.route("/auth/deleteaccount/<account_id>/", methods=["POST"])
@login_required
def auth_delete(account_id):
    user = User.query.get(account_id)
    articles = Artikkeli.query.get(account_id)
    db.session.delete(articles)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("auth_list_all_users"))

@app.route("/auth/reset_password/<account_id>/", methods=["POST"])
@login_required
def auth_reset_password(account_id):
    user = User.query.get(account_id)
    user.password = (request.form.get("password"))
    db.session().commit()

    return redirect(url_for("auth_list_all_users"))