from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ReportForm(FlaskForm):
    reason = TextAreaField("Reason", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Submit Report")
