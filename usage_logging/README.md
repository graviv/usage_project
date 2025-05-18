# 🌐 Cloud Table Usage Logging Playground

This repo contains simple SQL and Python scripts to help you **explore table usage and logging** in the three major cloud platforms:

- **Google Cloud Platform (BigQuery Sandbox)**
- **Amazon Web Services (Athena + S3 + CloudTrail)**
- **Microsoft Azure (Synapse Serverless + Log Analytics)**

## ✅ Objectives

- Create sample tables or datasets in each cloud
- Query them and monitor access or usage via logs
- Analyze usage with SQL or Python

## 🔷 Google Cloud Platform – BigQuery

### Sample SQL

```sql
CREATE SCHEMA IF NOT EXISTS my_dataset;
CREATE TABLE my_dataset.sample AS
SELECT 1 AS id, "hello" AS message;
```

### Analyze Usage

```sql
SELECT
  referenced_table_id,
  COUNT(*) AS query_count
FROM
  `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE
  creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY referenced_table_id
ORDER BY query_count DESC;
```

## 🟧 AWS – Athena + S3 + CloudTrail

### Sample SQL

```sql
CREATE DATABASE IF NOT EXISTS test_logs;

CREATE EXTERNAL TABLE test_logs.sample (
  id INT,
  message STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://<your-bucket>/sample.csv';
```

### CloudTrail Example

```sql
SELECT
  eventSource,
  eventName,
  resources[1].ARN AS table_arn,
  COUNT(*) AS usage_count
FROM
  cloudtrail_logs_database.cloudtrail_logs
WHERE
  eventSource = 'athena.amazonaws.com'
GROUP BY eventSource, eventName, resources[1].ARN
ORDER BY usage_count DESC;
```

## 🟦 Azure – Synapse Serverless + Log Analytics

### Sample SQL

```sql
SELECT * FROM OPENROWSET(
  BULK 'https://<yourstorage>.dfs.core.windows.net/data/sample.csv',
  FORMAT = 'CSV',
  PARSER_VERSION = '2.0'
) AS rows;
```

### Kusto Logs

```kusto
AzureDiagnostics
| where ResourceType == "SYNAPSE"
| where OperationName_s == "ExecuteSql"
| summarize count() by Statement_s
```

## 🐍 Python Scripts

- `bq_usage.py` – BigQuery usage
- `athena_usage.py` – AWS Athena + CloudTrail
- `azure_usage.py` – Azure Synapse + Log Analytics

Scripts in `/scripts/`

## 📦 Installation

```bash
pip install -r requirements.txt
```