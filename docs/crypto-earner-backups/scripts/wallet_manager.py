import json

def get_wallet(network):
    """
    Obtiene la dirección de wallet para una red específica.
    """
    try:
        config_path = "/home/jeengrasi/crypto-earner/config/wallet_config.json"
        with open(config_path, "r") as file:
            wallets = json.load(file)
            return wallets.get(network, "Wallet no configurada para esta red.")
    except Exception as e:
        print(f"Error al leer wallet config: {e}")
        return None
