from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MyForm(FlaskForm):
    name = StringField('name of image', validators=[DataRequired()])
    file = FileField('image file', validators=[ FileRequired(), FileAllowed(['png', 'jpeg', 'svg'], 'IMG file only!')])
    submit = SubmitField('Добавить')
    