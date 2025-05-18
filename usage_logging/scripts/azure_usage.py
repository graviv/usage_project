from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

query = '''
AzureDiagnostics
| where ResourceType == "SYNAPSE"
| where OperationName_s == "ExecuteSql"
| summarize count() by Statement_s
'''

workspace_id = "YOUR_WORKSPACE_ID"
response = client.query_workspace(workspace_id, query, timespan="P30D")
for table in response.tables:
    for row in table.rows:
        print(row)