from flask import render_template
from flask_login import login_required
from . import main_bp
from ..models import Post


@main_bp.route("/")
def home():
    published_posts = Post.query.filter_by(status="published").order_by(Post.date_posted.desc()).all()
    return render_template("home.html", posts=published_posts)


@main_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
