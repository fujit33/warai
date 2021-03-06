from flask_wtf import Form
from wtforms import StringField, TextAreaField,RadioField, widgets, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TodoForm(Form):
    title = StringField('title', validators=[DataRequired()], default='default')
    detail = TextAreaField('detail', validators=[Length(min=0, max=5000)])

class SurveyForm(Form):
    todofukens = []
    choice0 = RadioField('Choice0',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice1 = RadioField('Choice1',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice2 = RadioField('Choice2',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice3 = RadioField('Choice3',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice4 = RadioField('Choice4',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice5 = RadioField('Choice5',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice6 = RadioField('Choice6',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice7 = RadioField('Choice7',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice8 = RadioField('Choice8',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice9 = RadioField('Choice9',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice10 = RadioField('Choice10',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice11 = RadioField('Choice11',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice12 = RadioField('Choice12',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice13 = RadioField('Choice13',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice14 = RadioField('Choice14',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice15 = RadioField('Choice15',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice16 = RadioField('Choice16',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice17 = RadioField('Choice17',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice18 = RadioField('Choice18',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice19 = RadioField('Choice19',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice20 = RadioField('Choice20',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice21 = RadioField('Choice21',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice22 = RadioField('Choice22',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice23 = RadioField('Choice23',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice24 = RadioField('Choice24',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice25 = RadioField('Choice25',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice26 = RadioField('Choice26',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice27 = RadioField('Choice27',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice28 = RadioField('Choice28',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])
    choice29 = RadioField('Choice29',validators=[DataRequired()], choices=[("0", '解釈できない'),("1", "1"),("2","2"), ("3","3"),("4","4"),("5","5")])

    bokete = StringField('bokete', validators=[Length(min=0, max=500)])
    twitter = StringField('twitter', validators=[Length(min=0, max=500)])
    mail = StringField('mail', validators=[Length(min=0, max=500)])



