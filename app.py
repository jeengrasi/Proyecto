from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para manejar sesiones

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Validar usuario en la base de datos
        conn = sqlite3.connect('contactos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session["user_id"] = user[0]  # Guardar el ID del usuario en la sesión
            return redirect(url_for("mensajes"))
        else:
            return "Usuario o contraseña incorrectos", 401
    return render_template("login.html")

# Ruta protegida para mensajes
@app.route("/mensajes")
def mensajes():
    if "user_id" not in session:  # Verificar si el usuario está autenticado
        return redirect(url_for("login"))
    
    # Recuperar los mensajes de la base de datos
    conn = sqlite3.connect('contactos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, mensaje FROM mensajes")
    mensajes = cursor.fetchall()
    conn.close()
    
    return render_template("mensajes.html", mensajes=mensajes)

# Ruta de contacto
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        mensaje = request.form.get("mensaje")
        
        # Guardar mensaje en la base de datos
        conn = sqlite3.connect('contactos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mensajes (nombre, mensaje) VALUES (?, ?)", (nombre, mensaje))
        conn.commit()
        conn.close()
        
        return redirect(url_for("home"))
    return render_template("contacto.html")

# Ruta para cerrar sesión
@app.route("/logout")
def logout():
    session.pop("user_id", None)  # Eliminar el usuario de la sesión
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
