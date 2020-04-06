from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.artikkelit.models import Artikkeli
from application.artikkelit.forms import ArtikkeliForm
from application.author.models import Author

@app.route("/artikkelit", methods=["GET"])
@login_required
def artikkelit_index():
    return render_template("artikkelit/list.html", articles = Artikkeli.query.filter_by(account_id = current_user.id), 
    unread_articles=Artikkeli.list_unread_articles(current_user.id), 
    summary = Artikkeli.article_summary(current_user.id))

@app.route("/artikkelit/new/")
@login_required
def artikkelit_form():
    return render_template("artikkelit/new.html", form = ArtikkeliForm())


@app.route("/artikkelit/<artikkeli_id>/", methods=["POST"])
@login_required
def artikkeli_change_source(artikkeli_id):

    article = Artikkeli.query.get(artikkeli_id)
    article.source = (request.form.get("source"))
    db.session().commit()
  
    return redirect(url_for("artikkelit_index"))

@app.route("/artikkelit/read/<artikkeli_id>/", methods=["POST"])
@login_required
def artikkeli_set_read(artikkeli_id):
    article = Artikkeli.query.get(artikkeli_id)
    article.read = True
    db.session().commit()

    return redirect(url_for("artikkelit_index"))

@app.route("/artikkelit/delete/<artikkeli_id>/", methods=["POST"])
@login_required
def artikkeli_delete(artikkeli_id):
    
    article = Artikkeli.query.get(artikkeli_id)
    db.session().delete(article)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))

@app.route("/artikkelit/", methods=["POST"])
@login_required
def artikkelit_create():

    form = ArtikkeliForm(request.form)

    if not form.validate():
        return render_template("artikkelit/new.html", form = form)

    author = Author(form.authors.data)
    article = Artikkeli(form.name.data, [author], form.publisher.data, form.source.data, form.year.data)
    article.account_id = current_user.id

    db.session().add(article)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))
    

