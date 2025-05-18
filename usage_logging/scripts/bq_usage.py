from google.cloud import bigquery

client = bigquery.Client()
query = '''
SELECT
  referenced_table_id,
  COUNT(*) AS query_count
FROM
  `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE
  creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY referenced_table_id
ORDER BY query_count DESC
'''
df = client.query(query).to_dataframe()
print(df)