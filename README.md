# 🚀 Real-Time Data Platform (Kafka + Spark + FastAPI)

Plateforme de traitement de données **temps réel** basée sur **Apache Kafka**, **Apache Spark Structured Streaming** et **FastAPI**.

Ce projet fournit une **architecture complète, fonctionnelle et industrialisable**, adaptée à des cas d’usage métiers (finance, fiscalité, e‑commerce, monitoring, IoT).

---

## 🎯 Objectifs

* Ingestion de flux de données en temps réel
* Traitement streaming (nettoyage, agrégation, enrichissement)
* Stockage optimisé pour requêtes rapides
* Exposition via API REST
* Architecture scalable et résiliente

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
├── producer/
│   ├── producer.py
│   └── requirements.txt
│
├── spark/
│   ├── spark_streaming.py
│   └── requirements.txt
│
├── api/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
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