from flask_wtf import Form
from wtforms import StringField, TextAreaField,RadioField
from wtforms.validators import DataRequired, Length

class TodoForm(Form):
    title = StringField('title', validators=[DataRequired()])
    detail = TextAreaField('detail', validators=[Length(min=0, max=5000)])

class HyokaForm(Form):
    title = StringField('title', validators=[DataRequired()])
    detail = TextAreaField('detail', validators=[Length(min=0, max=5000)])
    choice_switcher = RadioField('Choice?',validators=[DataRequired()], choices=[('choice1', 'Choice One'), ('choice2', 'Choice Two')], default='choice1')