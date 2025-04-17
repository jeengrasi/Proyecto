import os
import subprocess

def obtener_archivos_locales(ruta):
    resultado = subprocess.run(["ls", "-R", ruta], capture_output=True, text=True)
    return resultado.stdout  # Eliminado `.decode()`

def obtener_archivos_drive():
    resultado = subprocess.run(["rclone", "ls", "proyecto:/Proyecto/"], capture_output=True, text=True)
    return resultado.stdout  # Eliminado `.decode()`

def obtener_archivos_github():
    resultado = subprocess.run(["git", "ls-tree", "-r", "main", "--name-only"], capture_output=True, text=True)
    return resultado.stdout  # Eliminado `.decode()`

def generar_documento():
    ruta_documento = os.path.expanduser("~/Proyecto/documento_proyecto.md")  # 🔹 Corrección para interpretar correctamente la ruta

    with open(ruta_documento, "w") as f:
        f.write("# 📌 Documentación del Proyecto\n\n")
        f.write("## 📂 Archivos Locales:\n" + obtener_archivos_locales(os.path.expanduser("~/Proyecto")) + "\n\n")
        f.write("## ☁️ Archivos en Google Drive:\n" + obtener_archivos_drive() + "\n\n")
        f.write("## 🛠️ Archivos en GitHub:\n" + obtener_archivos_github() + "\n\n")

    print(f"✅ Documento generado: {ruta_documento}")

generar_documento()
