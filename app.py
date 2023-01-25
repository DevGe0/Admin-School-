from flask import Flask, render_template, request, url_for, abort, redirect, flash
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect

from database import db
from forms import AlumnoForm
from forms import DocenteForm
from models import Alumno
from models import Docente
from modelUser import ModelUser
from User import User

# Indicamos el nombre del modulo actual
app = Flask(__name__)

# Configuracion de la BD
USER_DB = 'postgres'
PASS_DB = 'root'
URL_DB = 'localhost'
NAME_BD = 'admin_school_db'

# Cadena de conexion a postgres
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_BD}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
db.init_app(app)

# Configuramos Flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# Configuracion de flask-wft (llave secreta dificl de adivinar)
app.config['SECRET_KEY'] = 'llave_secreta'

# proteccion para formularios
csrf = CSRFProtect()
csrf.init_app(app)

# Pasamos la app.py al login_manager
login_manager_app = LoginManager(app)

# Creamos un metodo para manejar los login de los usuarios
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

# Creamos el metodo del index
@app.route('/')
def inicio():
    return render_template('index.html')

# Creamos el metodo de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                # si user y la contraseña estan bien hacemos login y lo agregamos a un loger
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('login.html')
        else:
            flash("User not found...")
            return render_template('login.html')
    else:
        return render_template('login.html')

# Creamos los metodos de home y logout
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Creamos los metodos para agg, ver, editar y eliminar alumno
@app.route('/estudiantes')
@login_required
def estudiantes():
    # Listado de todos los objetos de tipo Alumno
    #personas = Persona.query.all()
    # mostramos las personas  ordenadas por id
    alumnos = Alumno.query.order_by('id')
    total_alumnos = Alumno.query.count()
    app.logger.debug(f'Listado de alumnos: {alumnos}')
    app.logger.debug(f'Total de alumnos: {total_alumnos}')
    # Indicamos la pagina y variable con su valor
    return render_template('alumnos.html', alumnos=alumnos,  total_alumnos=total_alumnos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    alumno = Alumno()
    # Especificamos cual es nuestra clase de model con obj=
    alumnoForm = AlumnoForm(obj=alumno)
    if request.method == 'POST':
        # Validamos o enviamos el objeto indicado
        if alumnoForm.validate_on_submit():
            # llenamos el objeto con cada uno de los cambios del formulario
            alumnoForm.populate_obj(alumno)
            app.logger.debug(f'Alumno a insertar: {alumno}')
            # Insertamos el nuevo registro y guardamos en la db con commit
            db.session.add(alumno)
            db.session.commit()
            # redireccionamos al inicio
            return redirect(url_for('estudiantes'))
    # si es GET retornamos el formulario
    return render_template('agregar.html', forma = alumnoForm)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # Recuperamos el objeto persona a editar o manda error 404
    alumno = Alumno.query.get_or_404(id)
    # mostramos los valores recuperados del objeto persona
    alumnoForma = AlumnoForm(obj=alumno)
    if request.method == 'POST':
        # Validamos o enviamos el objeto indicado
        if alumnoForma.validate_on_submit():
            # llenamos el objeto con cada uno de los cambios del formulario
            alumnoForma.populate_obj(alumno)
            app.logger.debug(f'Alumno a actualizar: {alumno}')
            db.session.commit()
            return redirect(url_for('estudiantes'))
    return render_template('editar.html', forma=alumnoForma)

@app.route('/ver/<int:id>')
def ver_detalle(id):
    # recuperamos la persona segun el id indicado
    alumno = Alumno.query.get_or_404(id)
    app.logger.debug(f'Ver alumno: {alumno}')
    return render_template('detalle.html', alumno=alumno)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    alumno = Alumno.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar {alumno}')
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('estudiantes'))

# Creamos los metodos para agg, ver, editar y eliminar Docente
@app.route('/docentes')
@login_required
def docentes():
    # Listado de todos los objetos de tipo Alumno
    #personas = Persona.query.all()
    # mostramos las personas  ordenadas por id
    docentes = Docente.query.order_by('id')
    total_docentes = Docente.query.count()
    app.logger.debug(f'Listado de docentes: {docentes}')
    app.logger.debug(f'Total de docentes: {total_docentes}')
    # Indicamos la pagina y variable con su valor
    return render_template('docentes.html', docentes=docentes, total_docentes=total_docentes)

@app.route('/agregar2', methods=['GET', 'POST'])
def agregar2():
    docente = Docente()
    # Especificamos cual es nuestra clase de model con obj=
    docenteForm = DocenteForm(obj=docente)
    if request.method == 'POST':
        # Validamos o enviamos el objeto indicado
        if docenteForm.validate_on_submit():
            # llenamos el objeto con cada uno de los cambios del formulario
            docenteForm.populate_obj(docente)
            app.logger.debug(f'Docente a insertar: {docente}')
            # Insertamos el nuevo registro y guardamos en la db con commit
            db.session.add(docente)
            db.session.commit()
            # redireccionamos al inicio
            return redirect(url_for('docentes'))
    # si es GET retornamos el formulario
    return render_template('agregar2.html', forma=docenteForm)

@app.route('/editar2/<int:id>', methods=['GET', 'POST'])
def editar2(id):
    # Recuperamos el objeto persona a editar o manda error 404
    docente = Docente.query.get_or_404(id)
    # mostramos los valores recuperados del objeto persona
    docenteForma = DocenteForm(obj=docente)
    if request.method == 'POST':
        # Validamos o enviamos el objeto indicado
        if docenteForma.validate_on_submit():
            # llenamos el objeto con cada uno de los cambios del formulario
            docenteForma.populate_obj(docente)
            app.logger.debug(f'Docente a actualizar: {docente}')
            db.session.commit()
            return redirect(url_for('docentes'))
    return render_template('editar2.html', forma=docenteForma)

@app.route('/ver2/<int:id>')
def ver_detalle2(id):
    # recuperamos la persona segun el id indicado
    docente = Docente.query.get_or_404(id)
    app.logger.debug(f'Ver docente: {docente}')
    return render_template('detalle2.html', docente=docente)

@app.route('/eliminar2/<int:id>')
def eliminar2(id):
    docente = Docente.query.get_or_404(id)
    app.logger.debug(f'Docente a eliminar {docente}')
    db.session.delete(docente)
    db.session.commit()
    return redirect(url_for('docentes'))