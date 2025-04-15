# Guía para Sincronización de Archivos: Local, Rclone (Google Drive) y GitHub

Este documento describe cómo realizar la sincronización de archivos entre tu entorno local, Google Drive (usando Rclone) y GitHub de manera manual o automatizada.

## **1. Pasos para Sincronización Manual**

### **A. Sincronización Local**
1. **Crear o editar el archivo necesario**:
   Usa un editor de texto como `nano` para crear o editar el archivo, por ejemplo:
   ```bash
   nano informe_sincronizacion.md
   ```

2. **Confirmar que el archivo existe y está actualizado**:
   ```bash
   ls -la | grep informe_sincronizacion.md
   cat informe_sincronizacion.md
   ```

---

### **B. Subida a Google Drive con Rclone**
1. **Subir el archivo al remoto configurado (`proyecto`)**:
   ```bash
   rclone copyto informe_sincronizacion.md proyecto:informe_sincronizacion.md
   ```

2. **Verificar que el archivo se haya subido correctamente**:
   ```bash
   rclone ls proyecto: | grep informe_sincronizacion.md
   ```

---

### **C. Subida a GitHub**
1. **Agregar el archivo al repositorio local**:
   ```bash
   git add informe_sincronizacion.md
   ```

2. **Realizar un commit con un mensaje descriptivo**:
   ```bash
   git commit -m "Añadido informe de sincronización"
   ```

3. **Sincronizar con el repositorio remoto**:
   ```bash
   git pull origin main
   git push origin main
   ```

4. **Resolver conflictos (si los hay)**:
   - Editar los archivos con conflictos.
   - Marcar los conflictos resueltos:
     ```bash
     git add <archivo_en_conflicto>
     ```
   - Finalizar la fusión:
     ```bash
     git commit
     ```

---

## **2. Automatización del Proceso con un Script**

Puedes crear un script en **Bash** para automatizar este proceso. Aquí tienes un ejemplo:

```bash name=sync_project.sh
#!/bin/bash

# Variables
RCLONE_REMOTE="proyecto"
FILE="informe_sincronizacion.md"
GIT_BRANCH="main"

# 1. Verificar archivo local
echo "Verificando archivo local..."
if [ ! -f "$FILE" ]; then
    echo "El archivo $FILE no existe. Por favor, créalo antes de continuar."
    exit 1
fi

# 2. Subir archivo a Google Drive (Rclone)
echo "Subiendo archivo a Google Drive..."
rclone copyto "$FILE" "$RCLONE_REMOTE:$FILE"
if [ $? -ne 0 ]; then
    echo "Error al subir el archivo a Google Drive."
    exit 1
fi
echo "Archivo subido exitosamente a Google Drive."

# 3. Subir cambios a GitHub
echo "Subiendo cambios a GitHub..."
git add "$FILE"
git commit -m "Añadido informe de sincronización"
git pull origin "$GIT_BRANCH" --rebase
git push origin "$GIT_BRANCH"
if [ $? -ne 0 ]; then
    echo "Error al sincronizar con GitHub."
    exit 1
fi
echo "Cambios sincronizados con GitHub exitosamente."

# Finalización
echo "Sincronización completada."
```

### **Pasos para Usar el Script**
1. Crea el archivo del script:
   ```bash
   nano sync_project.sh
   ```
2. Pega el contenido del script anterior en el archivo.
3. Haz el script ejecutable:
   ```bash
   chmod +x sync_project.sh
   ```
4. Ejecuta el script siempre que necesites sincronizar:
   ```bash
   ./sync_project.sh
   ```

---

## **3. Automatización con Cron (Opcional)**
Para ejecutar el proceso automáticamente en intervalos regulares, utiliza **cron**:
1. Edita el archivo de tareas programadas:
   ```bash
   crontab -e
   ```
2. Agrega una línea para ejecutar el script, por ejemplo, todos los días a las 10:00 AM:
   ```bash
   0 10 * * * /ruta/a/tu/script/sync_project.sh
   ```

---

## **4. Verificación Final**
- **Localmente**: Asegúrate de que los archivos están actualizados.
- **Google Drive**: Verifica los archivos en el remoto con Rclone.
- **GitHub**: Revisa los commits y archivos en el repositorio remoto.

¡Con esta guía, puedes sincronizar tus archivos de manera sencilla y eficiente! 😊

