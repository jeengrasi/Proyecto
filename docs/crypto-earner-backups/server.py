"""
Servidor Flask para visualizar el progreso del proyecto Crypto Earner.
"""

import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    """
    Genera el dashboard con datos de oportunidades y faucets.
    """
    # Verificar si los archivos existen antes de cargarlos
    log_file = "/home/jeengrasi/crypto-earner/logs/faucet_api_log.txt"
    if not os.path.exists(log_file):
        open(log_file, "w").close()  # Crear archivo vacío si no existe

    opportunities_file = "/home/jeengrasi/crypto-earner/data/crypto_opportunities.csv"
    if not os.path.exists(opportunities_file):
        return "El archivo de oportunidades no existe. Por favor, ejecuta el análisis primero.", 500

    # Cargar los datos
    faucet_log = open(log_file).readlines()
    opportunities = pd.read_csv(opportunities_file)

    # Renderizar el dashboard
    return render_template("dashboard.html", opportunities=opportunities, faucet_log=faucet_log)

if __name__ == "__main__":
    app.run(debug=True)
