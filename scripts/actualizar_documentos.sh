#!/bin/bash

#   Variables
DOCUMENTO="$1"
NUEVA_INFORMACION="$2"
FECHA=$(date "+%Y-%m-%d %H:%M:%S")
HISTORIAL="historial_cambios.md"

#   Verificar si se proporcionaron el documento y la información
if [ -z "$DOCUMENTO" ] || [ -z "$NUEVA_INFORMACION" ]; then
  echo "Uso: $0 <documento.md> '<Nueva información>'"
  exit 1
fi

#   Añadir la nueva información al documento con la fecha
echo "##   Actualización: $FECHA" >> "$DOCUMENTO"
echo "$NUEVA_INFORMACION" >> "$DOCUMENTO"
echo "" >> "$DOCUMENTO"

#   Registrar la actualización en el historial de cambios
echo "##   Actualización de '$DOCUMENTO'" >> "$HISTORIAL"
echo "Fecha: $FECHA" >> "$HISTORIAL"
echo "Información Añadida: $NUEVA_INFORMACION" >> "$HISTORIAL"
echo "" >> "$HISTORIAL"

echo "✅ Documento '$DOCUMENTO' actualizado y registrado en '$HISTORIAL'."
