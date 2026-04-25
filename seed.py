from app import create_app
from app.extensions import db, bcrypt
from app.models import User, Post, Report

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# Admin
admin = User(username="admin", email="admin@example.com", role="admin")
admin.set_password("admin123")

# Regular user
user = User(username="alice", email="alice@example.com")
user.set_password("alice123")

db.session.add_all([admin, user])
db.session.commit()

# Sample post
sample = Post(
    title="Hello World",
    content="This is a published sample post.",
    status="published",
    author=user,
)
db.session.add(sample)
db.session.commit()

# Pending post and report
pending = Post(
    title="Needs Review",
    content="Pending moderation.",
    status="pending",
    author=user,
)
report = Report(
    reason="Offensive content",
    reporter_id=user.id,
    post=pending,
)
db.session.add_all([pending, report])
db.session.commit()

print("Database seeded.")
