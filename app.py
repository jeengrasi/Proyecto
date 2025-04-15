from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        # Aquí puedes procesar los datos del formulario
        nombre = request.form.get("nombre")
        mensaje = request.form.get("mensaje")
        print(f"Mensaje recibido de {nombre}: {mensaje}")
        # Redirigir al inicio después de enviar el formulario
        return redirect(url_for("home"))
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
