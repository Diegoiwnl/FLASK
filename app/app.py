from flask import Flask,render_template,redirect,url_for, request
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


@app.route('/Registrar' , methods=['GET','POST'] )
def registrar_usuario():
    if request.method == 'POST':
        Nombres = request.form.get('nombre')
        Apellidos = request.form.get('apellido')
        Email = request.form.get('correo')
        Direccion = request.form.get('direccion')
        Telefono = request.form.get('numero')
        Usuario = request.form.get('usuario')
        Contrasena = request.form.get('contrasena')

    #insertar datos a la tabla personas

        cursor.execute("INSERT INTO personas(nombreper,apellidoper,emailper,direccionper,telefonoper,usuarioper,contraseña) VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,Direccion,Telefono,Usuario,Contrasena))
        db.commit()


    #En el caso de que sea una solicitud, redirige a la misma pagina
    #cuando el método es post
        return redirect(url_for('registrar_usuario'))

    #Método get, renderiza el formulario
    return render_template('Registrar.html')

if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)
