import requests
import pandas as pd
import os
import pyarrow
from datetime import datetime

def get_crypto_data():
    print("🚀 Iniciando extración de datos de CoinGecko...")

    # URL de la API: Le peimos el precio de USD del Bitcoin, Ethereum y Solana
    url = "https://api.coingecko.com/api/v3/simple/price"
    parametros = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true'
    }

    # Hacemos la peticion a la pagina
    respuesta = requests.get(url, params=parametros)

    # Creamos una exepción para manejar errores en la ejecución
    try:
        # Si la página responde con un 200 (Éxito)
        if respuesta.status_code == 200:
            datos_json = respuesta.json()
            print("✅ ¡Datos obtenidos con éxito!")

            # Transformar ese JSON feo en una tabla bonita (DataFrame)
            df = pd.DataFrame.from_dict(datos_json, orient='index')

            # Le agregamos la fecha y la hora exactas en la que exrajimos el dato
            df['fecha_extraccion'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Reseteamos el indice para que el nombre de la moneda sea una columna
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'moneda'}, inplace=True)

            print("\n📊 Muestra de los datos en tiempo real:")
            #print(df)

            fecha_hoy = datetime.now().strftime("%Y-%m-%d")
            hora_minuto = datetime.now().strftime("%H%M")
        
            ruta_carpeta = f"data/raw/{fecha_hoy}"
            os.makedirs(ruta_carpeta, exist_ok=True)
            texto = (f"crypto_prices_{hora_minuto}.parquet")
            ruta_final = os.path.join(ruta_carpeta, texto)
            df.to_parquet(ruta_final, engine='pyarrow')
                    
            return ruta_final

        else:
            print(f"❌ Error al conectar con la API. Código: {respuesta.status_code}")

    except ValueError as e:
        print(f"❌ Error al procesar o guardar los datos {e}:")
        return None
    
if __name__ == "__main__":
    resultado = get_crypto_data()

    print(f"VALIDACION LOCAL: La funcion rertorno esto --- {resultado}")



