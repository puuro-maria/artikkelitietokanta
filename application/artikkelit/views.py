from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user
from sqlalchemy import or_

from application.artikkelit.models import Artikkeli
from application.artikkelit.forms import ArtikkeliForm
from application.author.models import Author
from application.keyword.models import Keyword
from application.articlekeyword.models import ArticleKeyword
from application.articleauthor.models import ArticleAuthor

@app.route("/artikkelit", methods=["GET"])
@login_required
def artikkelit_index():
    return render_template("artikkelit/list.html", articles = Artikkeli.query.filter_by(account_id = current_user.id), 
    unread_articles=Artikkeli.list_unread_articles(current_user.id), 
    summary = Artikkeli.article_summary(current_user.id))

@app.route("/search/", methods=["GET", "POST"])
@login_required
def artikkelit_search():
    wd = request.form.get("word")
    word = "%{}%".format(wd)
    preresults = db.session.query(Artikkeli).join(ArticleAuthor, Artikkeli.id == ArticleAuthor.article_id).join(Author, Author.id == ArticleAuthor.author_id).join(ArticleKeyword, Artikkeli.id == ArticleKeyword.article_id).join(Keyword, Keyword.id == ArticleKeyword.keyword_id).filter(or_((Artikkeli.name.like(word)), (Author.name.like(word)), (Keyword.name.like(word)), (Artikkeli.publisher.like(word)))).filter(Artikkeli.account_id == current_user.id)
    return render_template("search.html", results = preresults)

@app.route("/all", methods=["GET"])
@login_required(role="ADMIN")
def artikkelit_list_all():
    return render_template("artikkelit/listall.html", articles = Artikkeli.query.all())

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

    article = Artikkeli(form.name.data, form.publisher.data, form.source.data, form.year.data)

    article.account_id = current_user.id

    authors = form.authors.data.split(",")
    for a in authors:
        article.authors.append(Author(a))

    keywords = form.keywords.data.split(",")
    for k in keywords:
        article.keywords.append(Keyword(k))

    db.session().add(article)
    db.session().commit()

    return redirect(url_for("artikkelit_index"))
    
