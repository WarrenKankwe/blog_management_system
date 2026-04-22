from flask import render_template, redirect, url_for, flash, abort, request
from flask_login import current_user, login_required
from . import reports_bp
from .forms import ReportForm
from ..extensions import db, limiter
from ..models import Post, Report

report_rl = limiter.limit("5/minute")


@reports_bp.route("/new/<int:post_id>", methods=["GET", "POST"])
@login_required
@report_rl
def new_report(post_id):
    post = Post.query.get_or_404(post_id)
    if post.status != "published":
        abort(400)
    form = ReportForm()
    if form.validate_on_submit():
        report = Report(
            reason=form.reason.data,
            reporter_id=current_user.id,
            post_id=post.id,
        )
        db.session.add(report)
        db.session.commit()
        flash("Report submitted.", "info")
        return redirect(url_for("posts.post_detail", post_id=post.id))
    return render_template("report_form.html", form=form, post=post)
