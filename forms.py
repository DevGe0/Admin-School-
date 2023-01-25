from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AlumnoForm(FlaskForm):
    # indicamos q el nombre es un dato requerido
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido')
    email = StringField('Email', validators=[DataRequired()])
    edad = IntegerField('Edad')
    enviar = SubmitField('Enviar')

class DocenteForm(FlaskForm):
    # indicamos q el nombre es un dato requerido
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido')
    email = StringField('Email', validators=[DataRequired()])
    edad = IntegerField('Edad')
    enviar = SubmitField('Enviar')