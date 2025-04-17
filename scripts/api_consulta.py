from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>API en ejecución correctamente 🚀</h1>"

def obtener_datos():
    conn = sqlite3.connect('/home/jeengrasi/Proyecto/base_datos.db')  # 🔹 Ruta absoluta para evitar errores
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros")
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route('/consultar')
def consultar():
    datos = obtener_datos()
    return jsonify(datos)

@app.route('/consulta')  # 🔹 Nuevo endpoint agregado
def consulta_alias():
    return consultar()  # Redirige a la función `consultar`

if __name__ == '__main__':
    app.run(debug=True)
