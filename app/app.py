from flask import   *     #Flask,render_template
import mysql.connector
#Creamos una instancia de la clase Flask

app = Flask(__name__)

#CONFIGURAR LA CONEXIÓN
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda2024"


)
cursor = db.cursor()

#Definir rutas

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Registrar' , methods=['POST'] )
def registrar_usuario():
    Nombres = request.form['nombre'],
    Apellidos = request.form['apellido'],
    Email = request.form['correo'],
    Direccion = request.form['direccion'],
    Telefono = request.form['numero'],
    Usuario = request.form['usuario'],
    Contrasena = request.form['contrasena']

    #insertar datos a la tabla personas

    cursor.execute("INSERT IN TO personas(nombreper,apellidoper,emailper,dieccionper,telefonoper,usuarioper,contraseña)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,Direccion,Telefono,Usuario,Contrasena))
    db.commit()


    
    return redirect(url_for('/Registrar'))

if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)
