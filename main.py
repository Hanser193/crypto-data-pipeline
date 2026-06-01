import extract_crypto
import load_to_gcp
import os  # <-- Importamos os para manejar la ruta

def ejecutar_pipeline():
    print("Iniciando Pipeline...")
    
    # 1. Extraer
    direccion_en_mi_pc = extract_crypto.get_crypto_data() 
    print(f"✅ MAIN RECIBIÓ ESTA RUTA LOCAL: {direccion_en_mi_pc}")
    
    if direccion_en_mi_pc is not None:
        # 2. Armar la ruta dinámica para la nube
        # Esto extrae solo "crypto_prices_1058.parquet" de la ruta larga
        nombre_archivo = os.path.basename(direccion_en_mi_pc) 
        
        # Armamos la ruta destino en GCS (siempre usando '/' para la nube)
        direccion_en_la_nube = f"raw/crypto/{nombre_archivo}"
        print(f"☁️ DESTINO EN LA NUBE SERÁ: {direccion_en_la_nube}")
        
        # 3. Cargar a GCP
        load_to_gcp.subir_a_data_lake(direccion_en_mi_pc, direccion_en_la_nube)
        
        print("✅ Pipeline finalizado con éxito!")

if __name__ == "__main__":
    ejecutar_pipeline()