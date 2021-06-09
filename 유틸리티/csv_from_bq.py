from google.cloud import bigquery
import os
import csv
from datetime import date

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.getcwd()+KeyFilePath;

config = {
    'project': projectId,
    'dataset_id' : datasetId',
    'table_id' : tableId,
}

# Construct a BigQuery client object.
client = bigquery.Client()

query_table = config['project']+'.'+config['dataset_id']+'.'+config['table_id'];
table_schema = client.get_table(query_table).schema;

query = """
    SELECT *
    FROM `query_table`
"""
query_job = client.query(query)  # Make an API request.

print("schema save")
column_size = len(table_schema)
column = []
for row in table_schema:
    column.append(row.name)


#print("The query data:")
#for row in query_job:
#    print(row)
#    print(type(row[0]))


today = date.today()
today = today.strftime("%Y-%m-%d")
fileName = "pizzaseol_test_"+today+".csv"

with open('./../../file/'+fileName, mode='w') as query_result:
    csv_writer = csv.writer(query_result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(column)
    for row in query_job:
        tmp_row = []
        for i in range(column_size):
            tmp_row.append(row[i])
        csv_writer.writerow(tmp_row)
        tmp_row.clear()
