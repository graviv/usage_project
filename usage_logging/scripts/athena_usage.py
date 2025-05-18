import boto3
import time

athena = boto3.client('athena', region_name='us-east-1')

query = '''
SELECT eventSource, eventName, resources[1].ARN AS table_arn, COUNT(*) AS usage_count
FROM cloudtrail_logs_database.cloudtrail_logs
WHERE eventSource = 'athena.amazonaws.com'
GROUP BY eventSource, eventName, resources[1].ARN
ORDER BY usage_count DESC
'''

response = athena.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': 'cloudtrail_logs_database'},
    ResultConfiguration={'OutputLocation': 's3://your-bucket/query-results/'}
)

query_execution_id = response['QueryExecutionId']
print("Athena query started, execution ID:", query_execution_id)