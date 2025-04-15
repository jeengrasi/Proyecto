# Informe de Sincronización entre Local, Rclone (Google Drive) y GitHub

Este informe describe el estado actual del proyecto, su estructura y las integraciones configuradas para sincronización entre tu entorno local, Google Drive (usando Rclone), y el repositorio GitHub.

## 1. Estado Actual del Proyecto

### Estructura del Proyecto
El proyecto está organizado de forma modular para facilitar la expansión y el mantenimiento. La estructura incluye los componentes clave siguientes:

```plaintext
Proyecto/
├── docs/                 # Documentación
│   ├── informes/         # Informes detallados
│   └── estrategias/      # Estrategias y planes
├── db/                   # Base de datos
│   ├── contactos.db      # Archivo SQLite
│   └── backups/          # Respaldo automático
├── scripts/              # Scripts de automatización
│   ├── sincronizacion.py # Sincronización con GitHub y Rclone
│   └── auditoria.py      # Registro de cambios
├── logs/                 # Logs del sistema
│   ├── cambios.log       # Historial de cambios
│   └── errores.log       # Registro de errores
├── web/                  # Interfaz web
├── README.md             # Descripción del proyecto
└── flujo_autonomo_global.txt # Archivo de configuración o flujo
```

### Archivos Clave del Proyecto
1. **`app.py`:** Archivo principal que contiene la lógica del servidor usando Flask.
```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        mensaje = request.form.get("mensaje")
        print(f"Mensaje recibido de {nombre}: {mensaje}")
        return redirect(url_for("home"))
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
```

2. **`README.md`:** Documento que describe los objetivos y estructura del proyecto.

## 2. Sincronización Actual

### Local
- Archivos clave (`app.py`, `README.md`, `flujo_autonomo_global.txt`, `contactos.db`) están listos para sincronización.

### Rclone (Google Drive)
- **Remoto Configurado**: `proyecto`.
- **Comandos Probados**:
  ```bash
  rclone copyto flujo_autonomo_global.txt proyecto:flujo_autonomo_global.txt
  ```

### GitHub
- **Repositorio**: [Proyecto en GitHub](https://github.com/jeengrasi/Proyecto)
- **Estado del Repositorio**: Archivos correctamente versionados.
- **Comandos Probados**:
  ```bash
  git add .
  git commit -m "Actualización automática"
  git push origin main
  ```

## 3. Pasos para Guardar el Informe en Todas las Bases

### A. Guardar Localmente
1. Crea un archivo llamado `informe_sincronizacion.md`.
2. Pega este informe en el archivo y guárdalo.

### B. Subir a Google Drive (Rclone)
1. Usa el comando:
   ```bash
   rclone copyto informe_sincronizacion.md proyecto:informe_sincronizacion.md
   ```

### C. Subir a GitHub
1. Agrega el archivo al repositorio:
   ```bash
   git add informe_sincronizacion.md
   git commit -m "Añadido informe de sincronización"
   git push origin main
   ```
