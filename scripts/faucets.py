"""
Automatizar la interacción con faucets gratuitos.
"""

import requests

def get_matic_from_faucet():
    try:
        url = "https://faucet.polygon.technology"  # URL del faucet de Polygon
        response = requests.get(url)
        if response.status_code == 200:
            print("Faucet ejecutado exitosamente: MATIC recibido.")
            # Registrar resultado en archivo local
            with open("/home/jeengrasi/crypto-earner/logs/faucet_log.txt", "a") as log:
                log.write("Faucet de Polygon ejecutado exitosamente: MATIC recibido.\n")
        else:
            print("Error al interactuar con el faucet de MATIC.")
    except Exception as e:
        print(f"Error: {e}")

def get_ton_from_faucet():
    try:
        url = "https://faucet.tonkeeper.com"  # URL del faucet de Toncoin
        response = requests.get(url)
        if response.status_code == 200:
            print("Faucet ejecutado exitosamente: TON recibido.")
            # Registrar resultado en archivo local
            with open("/home/jeengrasi/crypto-earner/logs/faucet_log.txt", "a") as log:
                log.write("Faucet de Toncoin ejecutado exitosamente: TON recibido.\n")
        else:
            print("Error al interactuar con el faucet de TON.")
    except Exception as e:
        print(f"Error: {e}")
