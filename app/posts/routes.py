from flask import render_template, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from . import posts_bp
from .forms import PostForm
from ..extensions import db
from ..models import Post


@posts_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            status=form.status.data,
            author=current_user,
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("create_post.html", form=form)


def _verify_author(post):
    if post.author != current_user and not current_user.is_admin():
        abort(403)


@posts_bp.route("/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    _verify_author(post)
    if post.status != "draft":
        abort(403)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.status = form.status.data
        db.session.commit()
        flash("Post updated.", "info")
        return redirect(url_for("main.dashboard"))
    return render_template("create_post.html", form=form, legend="Update Post")


@posts_bp.route("/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    _verify_author(post)
    if post.status != "draft":
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "info")
    return redirect(url_for("main.dashboard"))


@posts_bp.route("/<int:post_id>")
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    # only published posts visible to everyone
    if post.status != "published" and post.author != current_user and not current_user.is_admin():
        abort(403)
    return render_template("post_detail.html", post=post)
