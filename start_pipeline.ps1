Write-Host "==============================="
Write-Host "🚀 START REAL-TIME PIPELINE"
Write-Host "==============================="

$KAFKA_HOME = "C:\kafka"
$SPARK_HOME = "C:\spark"
$PROJECT_DIR = "C:\realtime_exchange_platform"

# Zookeeper
Write-Host "🔹 Starting Zookeeper..."
Start-Process cmd -ArgumentList "/k $KAFKA_HOME\bin\windows\zookeeper-server-start.bat $KAFKA_HOME\config\zookeeper.properties"

Start-Sleep -Seconds 10

# Kafka
Write-Host "🔹 Starting Kafka broker..."
Start-Process cmd -ArgumentList "/k $KAFKA_HOME\bin\windows\kafka-server-start.bat $KAFKA_HOME\config\server.properties"

Start-Sleep -Seconds 15

# Spark Streaming
Write-Host "🔹 Starting Spark Streaming job..."
Start-Process cmd -ArgumentList "/k $SPARK_HOME\bin\spark-submit.cmd $PROJECT_DIR\spark_job.py"

Write-Host "✅ PIPELINE STARTED"
