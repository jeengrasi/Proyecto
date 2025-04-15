# Guía para Configurar y Ejecutar la Interfaz Web con Flask

Esta guía describe cómo configurar y ejecutar una interfaz web básica utilizando Flask en tu entorno de trabajo (iPad conectado por SSH a Linux en Chromebook).

---

## Requisitos Previos
1. **Entorno Virtual**:
   - Antes de instalar paquetes de Python, asegúrate de estar en un entorno virtual.
   - Crea el entorno virtual con:
     ```bash
     python3 -m venv venv
     ```
   - Activa el entorno:
     - En Linux/Mac: `source venv/bin/activate`
     - En Windows: `venv\Scripts\activate`

2. **Instalación de Flask**:
   - Instala Flask ejecutando:
     ```bash
     pip install flask
     ```

---

## Paso a Paso

### 1. Crear el Archivo Principal de la Aplicación
Crea un archivo llamado `app.py` con el siguiente contenido:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### 2. Crear la Carpeta para Plantillas
Crea una carpeta llamada `templates` y dentro de ella un archivo `index.html` con este contenido:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto - Sistema Autónomo</title>
</head>
<body>
    <h1>Bienvenido al Sistema Autónomo de Generación de Dinero</h1>
    <p>Este será el panel principal donde se visualizarán estadísticas y herramientas.</p>
</body>
</html>
```

### 3. Ejecutar la Aplicación
1. Asegúrate de estar en la misma carpeta donde se encuentra `app.py`.
2. Ejecuta:
   ```bash
   python app.py
   ```
3. Accede a la dirección `http://127.0.0.1:5000` en tu navegador.

---

## Notas
- Usa `Ctrl+C` en la terminal para detener la aplicación.
- Si encuentras algún error, verifica que todos los archivos estén correctamente nombrados y ubicados.
