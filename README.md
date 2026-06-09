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
## Bucket
<img width="1318" height="660" alt="image" src="https://github.com/user-attachments/assets/a3631829-6948-4188-8d26-9118cd59b8a0" />

## BigQuery
<img width="992" height="356" alt="image" src="https://github.com/user-attachments/assets/40c2ef7f-45a5-4d1f-9dae-b41292b55e57" />
