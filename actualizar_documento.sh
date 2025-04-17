#!/bin/bash

# Variables
DOC_MAESTRO="Sistema_Autonomo.md"
LOG_FILE="historial_cambios.md"

echo "🔍 Actualizando el Documento Maestro..."
echo "======================================" >> $DOC_MAESTRO
echo "Fecha: $(date)" >> $DOC_MAESTRO
echo "Evento: Nueva actualización del sistema" >> $DOC_MAESTRO
echo "" >> $DOC_MAESTRO

# 🔹 Registrar cambios en GitHub
echo "🔗 Estado del repositorio Git:" >> $DOC_MAESTRO
git status >> $DOC_MAESTRO
git log --oneline | head -5 >> $DOC_MAESTRO
echo "" >> $DOC_MAESTRO

# 🔹 Registrar archivos sincronizados con Rclone
echo "☁️ Archivos en Google Drive:" >> $DOC_MAESTRO
rclone ls proyecto: >> $DOC_MAESTRO
echo "" >> $DOC_MAESTRO

# 🔹 Registrar cambios en el historial
echo "Fecha: $(date) - Documento Maestro actualizado" >> $LOG_FILE

echo "✅ Actualización completada. Revisa el archivo: $DOC_MAESTRO"
