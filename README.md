# 🪙 Crypto Big Data Pipeline: Serverless & Apache Spark

Este proyecto es un pipeline de datos End-to-End diseñado para extraer, almacenar, procesar y disponibilizar datos financieros (Criptomonedas) utilizando una arquitectura moderna en la nube. 

El principal objetivo técnico de este proyecto es demostrar la automatización mediante infraestructura Serverless y la resolución del **"Small File Problem"** utilizando procesamiento distribuido con Apache Spark.

## 🏗️ Arquitectura del Proyecto

```mermaid
graph TD
    A[🌐 API CoinGecko] -->|Script en Python| B(⚡ Cloud Functions + Scheduler)
    B -->|Guarda particiones Parquet| C[(🪣 Cloud Storage - Capa Raw)]
    C -->|Lee miles de archivos| D[☄️ Apache Spark - Procesamiento]
    D -->|Agrupa y Limpia| E[(📊 BigQuery - Capa Gold)]
    E -->|Analítica de Negocio| F[📈 Power BI / Analistas]
```

⚙️ Flujo de Datos (Paso a Paso)
Extracción (Ingesta): Un script modular en Python consume la API pública de CoinGecko para obtener el precio y volumen del Bitcoin, Ethereum y Solana en tiempo real.
Orquestación Autónoma: El código está desplegado en Google Cloud Functions y orquestado mediante Cloud Scheduler para ejecutarse automáticamente cada hora, las 24 horas del día (Micro-batching).
Data Lake (Capa Bronce): Los datos en bruto aterrizan en un bucket de Google Cloud Storage en formato columnar óptimo (.parquet), particionados automáticamente por fecha y hora.
Procesamiento Distribuido: Para procesar el historial acumulado y evitar cuellos de botella por múltiples archivos pequeños, se utiliza Apache Spark (PySpark), agrupando la información y calculando promedios y máximos históricos.
Data Warehouse (Capa Oro): El DataFrame final procesado se inyecta directamente en Google BigQuery, listo para ser consumido por analistas de negocio en herramientas de BI.

🛠️ Stack Tecnológico
Lenguaje: Python 3.11 (Pandas, PyArrow, Requests)
Big Data Engine: Apache Spark (PySpark)
Cloud Provider (GCP):
Compute: Cloud Functions, Cloud Scheduler
Storage: Cloud Storage (GCS)
Data Warehouse: BigQuery
Entorno de Procesamiento: Google Colab / Databricks

📸 Evidencia de Ejecución en la Nube
Para validar la correcta ejecución y automatización del pipeline, aquí presento la evidencia de los datos aterrizando en las distintas capas de Google Cloud Platform:
1. Data Lake (Google Cloud Storage)
Aquí se observa cómo el Cloud Scheduler ejecuta la función Serverless cada hora, depositando los archivos Parquet de forma automatizada.
![alt text](bucket_gcs.png)
<img width="1318" height="660" alt="image" src="https://github.com/user-attachments/assets/a3631829-6948-4188-8d26-9118cd59b8a0" />

2. Data Warehouse (Google BigQuery)
Aquí se evidencia el resultado final tras el procesamiento distribuido con Apache Spark. Los datos limpios, agregados y transformados aterrizan en la tabla analítica final.
![alt text](tabla_bigquery.png)
<img width="992" height="356" alt="image" src="https://github.com/user-attachments/assets/40c2ef7f-45a5-4d1f-9dae-b41292b55e57" />

🚀 Cómo replicar este proyecto
Si deseas ejecutar la etapa de ingesta localmente antes de desplegarla en Cloud Functions:
Clona este repositorio:
code
Bash
git clone https://github.com/TuUsuario/crypto-data-pipeline.git
cd crypto-data-pipeline

Instala las dependencias:
code
Bash
pip install -r requirements.txt
Ejecuta el pipeline principal:
code
Bash
python main.py
Desarrollado por [Brayan Smith Hanser] - Data Engineer


code

***

### 🛠️ Últimos pasos después de pegar el texto:

1. Reemplaza `[Tu Nombre]` al final del documento.
2. Reemplaza `TuUsuario` en el link del paso 1 de clonación por tu usuario real de GitHub (`Hanser193`).
3. Revisa que los nombres de las imágenes en los paréntesis `(bucket_gcs.png)` y `(tabla_bigquery.png)` coincidan **exactamente** con los archivos de imágenes que metiste en tu carpeta (respeta mayúsculas y minúsculas).
4. Guarda el archivo, y ejecuta tu triada de Git:
   * `git add .`
   * `git commit -m "Actualización del README con arquitectura, evidencias de GCS y BigQuery"`
   * `git push`

