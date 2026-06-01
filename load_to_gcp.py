from google.cloud import storage

# 1. Configuraciones
BUCKET_NAME = 'brayan-data-lake-olist' 

def subir_a_data_lake(ruta_local, nombre_del_archivo):
    # Conexión a Google Cloud
    print("☁️ Conectando a Google Cloud Storage...")
    # ¡Magia! Aquí Python usa las credenciales que configuraste en la consola
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    
    # Subir el archivo
    blob = bucket.blob(nombre_del_archivo)
    blob.upload_from_filename(ruta_local)
    
    print("✅ ¡Carga exitosa! El archivo ya está en tu Data Lake.")
    return True

if __name__ == "__main__":
    subir_a_data_lake