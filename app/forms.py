from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, widgets, SelectMultipleField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MyForm(FlaskForm):
    name = StringField('name of image', validators=[DataRequired()])
    file = FileField('image file', validators=[ FileRequired(), FileAllowed(['png', 'jpeg', 'svg'], 'IMG file only!')])
    submit = SubmitField('Добавить')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
    list_of_ingr = [('potato','Картошка'),('tomato','Помидор'),('carrot','Морковь')]

    files1 = []
    files2 = []
    files3 = []
    for x in list_of_ingr: #split in 3 inputs
        if(list_of_ingr.index(x) % 3 == 0):
            files1.append(x)
        elif(list_of_ingr.index(x) % 2 == 0):
            files2.append(x)
        else:
            files3.append(x)

    cb1 = MultiCheckboxField('ingr_1', choices=files1)
    cb2 = MultiCheckboxField('ingr_2', choices=files2)
    cb3 = MultiCheckboxField('ingr_3', choices=files3)