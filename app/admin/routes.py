from flask import render_template, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from . import admin_bp
from ..extensions import db
from ..models import Post, Report


def admin_required():
    if not current_user.is_authenticated or not current_user.is_admin():
        abort(403)


@admin_bp.route("/moderation")
@login_required
def moderation_panel():
    admin_required()
    pending_posts = Post.query.filter_by(status="pending").all()
    pending_count = Post.query.filter_by(status="pending").count()
    report_count  = Report.query.filter_by(status="open").count()
    return render_template(
        "admin_moderation.html",
        posts=pending_posts,
        pending_count=pending_count,
        report_count=report_count,
    )


@admin_bp.route("/moderation/<int:post_id>/<string:action>")
@login_required
def moderate_post(post_id, action):
    admin_required()
    post = Post.query.get_or_404(post_id)
    if action == "publish":
        post.status = "published"
    elif action == "remove":
        post.status = "removed"
    else:
        abort(400)
    db.session.commit()
    flash("Post status updated.", "success")
    return redirect(url_for("admin.moderation_panel"))


@admin_bp.route("/reports")
@login_required
def reports_panel():
    admin_required()
    reports = Report.query.filter_by(status="open").all()
    pending_count = Post.query.filter_by(status="pending").count()
    report_count  = len(reports)
    return render_template(
        "admin_reports.html",
        reports=reports,
        pending_count=pending_count,
        report_count=report_count,
    )


@admin_bp.route("/reports/<int:report_id>/<string:action>")
@login_required
def review_report(report_id, action):
    admin_required()
    report = Report.query.get_or_404(report_id)
    if action == "keep":
        report.status = "reviewed"
    elif action == "remove":
        report.status = "reviewed"
        report.post.status = "removed"
    else:
        abort(400)
    db.session.commit()
    flash("Report processed.", "success")
    return redirect(url_for("admin.reports_panel"))
