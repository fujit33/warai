from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class TodoForm(Form):
    title = StringField('title', validators=[DataRequired()])
    detail = TextAreaField('detail', validators=[Length(min=0, max=5000)])