"""
Manejador de faucets para automatización de reclamos de criptomonedas.
"""

import requests

def interact_with_polygon_faucet():
    """
    Interactúa con el faucet de Polygon automáticamente.
    """
    try:
        url = "https://faucet.polygon.technology"
        wallet_address = "0xEC810a2149755D1AE051311E650265d316Ed1834"  # Dirección Metamask
        data = {"address": wallet_address}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            print("MATIC reclamados exitosamente.")
            with open("/home/jeengrasi/crypto-earner/logs/faucet_log.txt", "a") as log:
                log.write("Polygon Faucet ejecutado exitosamente: MATIC reclamados.\n")
        elif response.status_code == 403:
            print("Acceso denegado (403). Posible restricción de IP o datos faltantes.")
        else:
            print(f"Error en el faucet de Polygon: {response.status_code}")
    except Exception as e:
        print(f"Error al interactuar con el faucet de Polygon: {e}")

def interact_with_bsc_testnet_faucet():
    """
    Interactúa con el faucet de Binance Smart Chain Testnet automáticamente.
    """
    try:
        url = "https://testnet.binance.org/faucet-smart"
        wallet_address = "0xEC810a2149755D1AE051311E650265d316Ed1834"  # Dirección Metamask
        data = {"address": wallet_address}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            print("BNB Testnet tokens reclamados exitosamente.")
            with open("/home/jeengrasi/crypto-earner/logs/faucet_log.txt", "a") as log:
                log.write("BSC Testnet Faucet ejecutado exitosamente: BNB Testnet tokens reclamados.\n")
        elif response.status_code == 403:
            print("Acceso denegado al faucet de BSC Testnet (403).")
        else:
            print(f"Error en el faucet de BSC Testnet: {response.status_code}")
    except Exception as e:
        print(f"Error al interactuar con el faucet de BSC Testnet: {e}")

def run_faucets_manager():
    """
    Ejecuta todos los faucets configurados automáticamente.
    """
    print("Iniciando gestión de faucets...")
    interact_with_polygon_faucet()
    interact_with_bsc_testnet_faucet()
    print("Gestión de faucets completada.")
