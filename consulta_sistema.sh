#!/bin/bash

# Variables
REPO_URL="https://github.com/jeengrasi/Proyecto"  # URL de tu repositorio
RCLONE_REMOTE="proyecto"  # Nombre del remoto en Rclone
OUTPUT_FILE="consulta_sistema.md"  # Documento donde se registrará la información

echo "🔍 Consultando archivos en el sistema..." > $OUTPUT_FILE
echo "Fecha: $(date)" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# 🔹 Listar archivos en GitHub (Local)
echo "🗂️ Archivos en GitHub (Local):" >> $OUTPUT_FILE
ls -R >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# 🔹 Obtener estado del repositorio Git
echo "🔗 Estado del repositorio Git:" >> $OUTPUT_FILE
git status >> $OUTPUT_FILE
git log --oneline | head -10 >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# 🔹 Listar archivos en Google Drive con Rclone
echo "☁️ Archivos en Google Drive (Rclone):" >> $OUTPUT_FILE
rclone ls $RCLONE_REMOTE: >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

echo "✅ Consulta completa. Revisa el archivo: $OUTPUT_FILE"
