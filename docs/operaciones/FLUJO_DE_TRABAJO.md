# Flujo de Trabajo para Guardar y Validar Cambios

Este documento explica cómo se manejan los cambios en el proyecto y cómo puedes validarlos localmente.

---

## Proceso para Guardar Cambios
1. **Creación o Actualización de Archivos**:
   - Cada archivo que se cree o actualice será automáticamente subido al repositorio remoto.
   - Se agregará un mensaje de commit claro para que puedas rastrear los cambios realizados.

2. **Sincronización Local**:
   - Después de subir los cambios al repositorio remoto, podrás obtenerlos localmente ejecutando:
     ```bash
     git pull
     ```

---

## Cómo Validar Localmente
1. Accede al entorno Linux en tu Chromebook utilizando SSH desde tu iPad.
2. Navega a la carpeta del proyecto:
   ```bash
   cd /ruta/a/tu/proyecto
   ```
3. Asegúrate de tener los últimos cambios:
   ```bash
   git pull
   ```
4. Abre los archivos para revisarlos o editarlos usando un editor como `nano` o `vim`.

5. **Ejecuta los scripts o prueba los cambios**:
   - Sigue los pasos documentados en las guías (por ejemplo, `docs/GUIA_Flask.md`).

---

## Notas Importantes
- **Edición de Scripts**:
  - Si necesitas modificar un script, elimina el archivo existente y crea uno nuevo con las modificaciones necesarias.
  - Esto asegura que el sistema se mantenga limpio y organizado.

- **Confirmación de Cambios**:
  - Siempre valida los cambios localmente antes de continuar con nuevas implementaciones.
