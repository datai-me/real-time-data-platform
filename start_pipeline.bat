@echo off
echo ================================
echo 🚀 START REAL-TIME PIPELINE
echo ================================

REM === CONFIGURATION ===
SET KAFKA_HOME=C:\kafka
SET SPARK_HOME=C:\spark
SET PROJECT_DIR=C:\realtime_exchange_platform

REM === START ZOOKEEPER ===
echo 🔹 Starting Zookeeper...
start cmd /k "%KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties"

timeout /t 10

REM === START KAFKA ===
echo 🔹 Starting Kafka broker...
start cmd /k "%KAFKA_HOME%\bin\windows\kafka-server-start.bat %KAFKA_HOME%\config\server.properties"

timeout /t 15

REM === START SPARK STREAMING ===
echo 🔹 Starting Spark Streaming job...
start cmd /k "%SPARK_HOME%\bin\spark-submit.cmd %PROJECT_DIR%\spark_job.py"

echo ================================
echo ✅ PIPELINE STARTED SUCCESSFULLY
echo ================================
pause
