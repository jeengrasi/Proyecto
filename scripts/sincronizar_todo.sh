#!/bin/bash

MENSAJE_BASE="Actualización automática"
FECHA=$(date "+%Y-%m-%d %H:%M:%S")
LOG_FILE="sincronizacion.log"

# Función para registrar mensajes
log() {
  FECHA_LOG=$(date "+%Y-%m-%d %H:%M:%S")
  echo "$FECHA_LOG - $1" >> "$LOG_FILE"
}

log "Iniciando el script de sincronización."

echo "🔄 Verificando cambios en Git..."
log "Verificando cambios en Git..."
CAMBIOS=$(git status --porcelain)

if [ -z "$CAMBIOS" ]; then
  echo "✅ No hay cambios locales para commitear."
  log "No hay cambios locales para commitear."
else
  echo "📝 Cambios detectados:"
  log "Cambios detectados:"
  echo "$CAMBIOS"
  log "$CAMBIOS"
  echo ""
  echo "Añadiendo todos los cambios..."
  log "Añadiendo todos los cambios..."
  git add .

  # Crear un resumen de los archivos modificados para el mensaje del commit
  ARCHIVOS_MODIFICADOS=$(git diff --name-only --cached)
  MENSAJE_COMMIT="$MENSAJE_BASE: $FECHA - Archivos modificados: $ARCHIVOS_MODIFICADOS"

  echo "💾 Commiteando cambios con el mensaje: '$MENSAJE_COMMIT'"
  log "Commiteando cambios con el mensaje: '$MENSAJE_COMMIT'"
  git commit -m "$MENSAJE_COMMIT"

  echo "📤 Subiendo cambios al repositorio remoto..."
  log "Subiendo cambios al repositorio remoto..."
  git push origin main
fi

echo ""
echo "☁️ Sincronizando con Google Drive (Rclone)..."
log "Sincronizando con Google Drive (Rclone)..."
rclone sync . Proyecto: --exclude ".git/" --exclude "*.swp" --exclude "*.swo" -v
RCLONE_EXIT_CODE=$?

if [ $RCLONE_EXIT_CODE -eq 0 ]; then
  echo "✅ Sincronización con Google Drive completada."
  log "Sincronización con Google Drive completada."
else
  echo "⚠️ Posibles problemas con la sincronización de Google Drive (código de salida: $RCLONE_EXIT_CODE)."
  log "Posibles problemas con la sincronización de Google Drive (código de salida: $RCLONE_EXIT_CODE)."
fi

echo "✅ Proceso de sincronización finalizado."
log "Proceso de sincronización finalizado."
