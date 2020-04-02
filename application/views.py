from flask import render_template
from application import app
from application.artikkelit.models import Artikkeli
from flask_login import login_required, current_user

@app.route("/")
def index():
    return render_template("index.html")
    
