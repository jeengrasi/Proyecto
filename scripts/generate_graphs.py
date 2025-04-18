"""
Generar gráficos de análisis a partir de los datos de oportunidades.
"""

import pandas as pd
import matplotlib.pyplot as plt

def generate_graph():
    """
    Crea un gráfico de barras a partir de las oportunidades de inversión en criptomonedas.
    """
    try:
        file_path = "/home/jeengrasi/crypto-earner/data/crypto_opportunities.csv"
        df = pd.read_csv(file_path)

        # Configuración del gráfico
        plt.figure(figsize=(10, 6))
        plt.bar(df['name'], df['price_change_percentage_24h'], color='skyblue')
        plt.title('Oportunidades de inversión (Incremento % en 24h)', fontsize=14)
        plt.xlabel('Criptomoneda', fontsize=12)
        plt.ylabel('% de Incremento', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Guardar el gráfico como imagen
        graph_path = "/home/jeengrasi/crypto-earner/data/crypto_graph.png"
        plt.savefig(graph_path)
        print(f"Gráfico generado y guardado en: {graph_path}")
        return graph_path
    except Exception as e:
        print(f"Error al generar gráfico: {e}")
        return None
