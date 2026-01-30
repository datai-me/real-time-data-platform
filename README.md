# 🚀 Real-Time Data Platform (Kafka + Spark + FastAPI)

Plateforme de traitement de données **temps réel** basée sur **Apache Kafka**, **Apache Spark Structured Streaming** et **FastAPI**.

Ce projet fournit une **architecture complète, fonctionnelle et industrialisable**, adaptée à des cas d’usage métiers (finance, fiscalité, e‑commerce, monitoring, IoT).

---

## 🎯 Objectifs

* Ingestion **horaire automatique** des taux de change (API publique)
* Orchestration avec **Apache Airflow**
* Traitement temps réel avec **Spark Structured Streaming**
* Détection d’anomalies (variations anormales)
* Stockage analytique et exposition via API REST

---

## 🧱 Architecture détaillée

```
┌──────────────┐
│ Data Sources │
│ (Apps, IoT)  │
└──────┬───────┘
       │ JSON
┌──────▼───────┐
│   Kafka      │
│  (Topics)   │
└──────┬───────┘
       │ Stream
┌──────▼─────────────────────┐
│ Spark Structured Streaming │
│ - filtering                │
│ - aggregation              │
│ - windowing                │
└──────┬─────────────────────┘
       │
┌──────▼───────────┐
│ PostgreSQL /     │
│ Redis            │
└──────┬───────────┘
       │ SQL
┌──────▼───────────┐
│ FastAPI          │
│ REST API         │
└──────┬───────────┘
       │
┌──────▼───────────┐
│ Clients / BI     │
│ Dashboards       │
└──────────────────┘
```

---

## 🗂 Structure du projet

```
real-time-data-platform/
│
├── docker-compose.yml
├── README.md
│
├── airflow/
│   ├── dags/
│   │   └── exchange_rate_dag.py
│   └── requirements.txt
│
├── producer/
│   └── exchange_rate_producer.py
│
├── spark/
│   └── spark_anomaly_detection.py
│
├── api/
│   ├── main.py
│   └── database.py
│
└── sql/
    └── init.sql
```

---

## ⚙️ Technologies

* **Python 3.10+**
* **Apache Kafka**
* **Apache Spark 3.x**
* **PostgreSQL**
* **FastAPI**
* **Docker / Docker Compose**