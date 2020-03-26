from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.artikkelit.models import Artikkeli
from application.artikkelit.forms import ArtikkeliForm

@app.route("/artikkelit", methods=["GET"])
@login_required
def artikkelit_index():
    return render_template("artikkelit/list.html", artikkelit = Artikkeli.query.all())

@app.route("/artikkelit/new/")
@login_required
def artikkelit_form():
    return render_template("artikkelit/new.html", form = ArtikkeliForm())


@app.route("/artikkelit/<artikkeli_id>/", methods=["POST"])
@login_required
def artikkeli_change_source(artikkeli_id):

    a = Artikkeli.query.get(artikkeli_id)
    a.source = (request.form.get("source"))
    db.session().commit()
  
    return redirect(url_for("artikkelit_index"))

@app.route("/artikkelit/delete/<artikkeli_id>/", methods=["POST"])
@login_required
def artikkeli_delete(artikkeli_id):
    
    a = Artikkeli.query.get(artikkeli_id)
    db.session().delete(a)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))

@app.route("/artikkelit/", methods=["POST"])
@login_required
def artikkelit_create():

    form = ArtikkeliForm(request.form)

    #if not form.validate():
     #   return render_template("artikkelit/new.html", form = form)

    a = Artikkeli(form.name.data, form.publisher.data, form.source.data, form.year.data)
    a.account_id = current_user.id

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))

