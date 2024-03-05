from flask import Flask,render_template,redirect,url_for,flash,request
import mysql.connector
#Creamos una instancia de la clase Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'
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
def lista():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM personas')
    usuario =  cursor.fetchall()

    return render_template('index.html', personas=usuario)


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
        flash('Usuario creado correctamente','success')



    #En el caso de que sea una solicitud, redirige a la misma pagina
    #cuando el método es post
        return redirect(url_for('registrar_usuario'))

    #Método get, renderiza el formulario
    return render_template('Registrar.html')

@app.route('/Editar/<int:id>' ,methods = ['GET','POST'])
def editar_usuario(id):
    cursor = db.cursor()
    if request.method == 'POST':
        nombrepersona = request.form.get('nombrepersona')
        apellidopersona = request.form.get('apellidopersona')
        emailpersona = request.form.get('emailpersona')
        direccionpersona = request.form.get('direccionpersona')
        telefonopersona = request.form.get('telefonopersona')
        usuariopersona = request.form.get('usuariopersona')
        contraseñapersona = request.form.get('contraseñapersona')

    #sentencia para actualizar los datos
        sql = "UPDATE personas set nombreper=%s,apellidoper=%s,emailper=%s,direccionper=%s,telefonoper=%s,usuarioper=%s,contraseña=%s where polper=%s"
        cursor.execute(sql,(nombrepersona,apellidopersona,emailpersona,direccionpersona,telefonopersona,usuariopersona,contraseñapersona,id))
        db.commit()

        return redirect(url_for('lista'))
    else:
        #obtener los datos de la persona que va a editar
        cursor = db.cursor()
        cursor.execute('SELECT * FROM personas WHERE polper = %s', (id,))
        data = cursor.fetchall()

        return render_template('Editar.html' , personas=data[0])

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_usuario(id):
    
    return redirect(url_for('lista'))






if __name__ == '__main__':
    app.add_url_rule('/',view_func=lista)
    app.run(debug=True,port=5005)
