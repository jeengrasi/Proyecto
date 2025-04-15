"""
Análisis avanzado usando la API pública de CoinGecko.
"""

import requests
import pandas as pd

def analyze_cryptos():
    """
    Obtiene datos en tiempo real de CoinGecko y filtra criptomonedas
    según criterios de cambio de precio y capitalización.
    """
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Crear un DataFrame
        df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]
        filtered_df = df[df['price_change_percentage_24h'] > 3]  # Filtra criptos con más del 3% incremento
        file_path = "/home/jeengrasi/crypto-earner/data/crypto_opportunities.csv"
        filtered_df.to_csv(file_path, index=False)

        print(f"Análisis completado y guardado en: {file_path}")
        return file_path
    except Exception as e:
        print(f"Error al realizar el análisis: {e}")
        return None
