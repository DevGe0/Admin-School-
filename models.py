# Definimos nuestra clase de modelo con la clase Model
from app import db


class Alumno(db.Model):
    # definimos una columna de tipo entera y llave primaria para la tabla de bd
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    edad = db.Column(db.Integer)

    # definimos el metodo str
    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Email: {self.email},'
            f'Edad: {self.edad}'
        )

class Docente(db.Model):
    # definimos una columna de tipo entera y llave primaria para la tabla de bd
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    edad = db.Column(db.Integer)

    # definimos el metodo str
    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Email: {self.email},'
            f'Edad: {self.edad}'
        )

class Login(db.Model):
    # definimos una columna de tipo entera y llave primaria para la tabla de bd
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(250))
    fullname = db.Column(db.String(250))

    # definimos el metodo str
    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Username: {self.nombre}, '
            f'Password: {self.apellido}, '
            f'Fullname: {self.fullname}, '
        )