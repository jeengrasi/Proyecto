"""
Script para actualizar las memorias del proyecto automáticamente.
"""

import datetime

def actualizar_memorias(resumen, detalles):
    """
    Actualiza ambos documentos con los avances recientes del proyecto.
    :param resumen: Resumen breve para la memoria personal.
    :param detalles: Detalles completos para el proyecto.
    """
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Actualizar memoria personal
    with open("/home/jeengrasi/crypto-earner/copilot_memory.txt", "a") as memoria_personal:
        memoria_personal.write(f"\nFecha: {fecha}\n{resumen}\n")

    # Actualizar proyecto completo
    with open("/home/jeengrasi/crypto-earner/project_full_log.txt", "a") as memoria_completa:
        memoria_completa.write(f"\nFecha: {fecha}\n{detalles}\n")

# Ejemplo de actualización
if __name__ == "__main__":
    resumen = "Script principal ejecutado con éxito; archivo respaldado en Google Drive; notificación enviada."
    detalles = """Se ejecutó el flujo automatizado, incluyendo análisis avanzado, respaldo y notificación. 
    Resultados: archivo crypto_opportunities.csv generado."""
    
    actualizar_memorias(resumen, detalles)
