from application import app, db
from flask import redirect, render_template, request, url_for
from application.artikkelit.models import Artikkeli

@app.route("/artikkelit", methods=["GET"])
def artikkelit_index():
    return render_template("artikkelit/list.html", artikkelit = Artikkeli.query.all())

@app.route("/artikkelit/new/")
def artikkelit_form():
    return render_template("artikkelit/new.html")

@app.route("/artikkelit/", methods=["POST"])
def artikkelit_create():
    a = Artikkeli(request.form.get("name"))

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))