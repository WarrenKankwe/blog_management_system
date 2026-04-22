from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired()])
    status = SelectField(
        "Status",
        choices=[("draft", "Draft"), ("pending", "Submit for Review")],
        default="draft",
    )
    submit = SubmitField("Save")
