from datetime import datetime
from .extensions import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")
    posts = db.relationship("Post", backref="author", lazy=True)

    def set_password(self, pw):
        self.password_hash = bcrypt.generate_password_hash(pw).decode("utf-8")

    def check_password(self, pw):
        return bcrypt.check_password_hash(self.password_hash, pw)

    def is_admin(self):
        return self.role == "admin"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(
        db.String(15), nullable=False, default="draft"
    )  # draft|pending|published|removed
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    reports = db.relationship("Report", backref="post", lazy=True)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(10), default="open")  # open|reviewed
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
    reporter_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
