from scripts.setup_xmrig import setup_xmrig
from scripts.wallet_manager import get_wallet

def main():
    try:
        print("Iniciando configuración automática...")

        # Configurar XMRig
        setup_xmrig()

        # Obtener dirección de wallet
        monero_wallet = get_wallet("Monero")
        print(f"Wallet Monero configurada: {monero_wallet}")

        print("Configuración completada exitosamente.")
    except Exception as e:
        print(f"Error en el flujo principal: {e}")

if __name__ == "__main__":
    main()
