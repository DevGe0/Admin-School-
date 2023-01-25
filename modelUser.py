from User import User
import psycopg2
conexion = psycopg2.connect(
    user= 'postgres',
    password = 'root',
    host= '127.0.0.1',
    port= '5432',
    database='admin_school_db'
)

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sql = """SELECT id, username, password, fullname FROM login 
                                WHERE username = '{}'""".format(user.username)
                    cursor.execute(sql)
                    row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sql = "SELECT id, username, fullname FROM login WHERE id = '{}'".format(id)
                    cursor.execute(sql)
                    row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)