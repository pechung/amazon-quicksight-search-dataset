import boto3

client = boto3.client('quicksight')
acctid = <Insert Account ID here>


#retrieving a list of data set IDs for the given aws account 
data_sets = client.list_data_sets(
    AwsAccountId=acctid
)
data_set_ids = [data_sets['DataSetSummaries'][i]['DataSetId'] for i in range(len(data_sets['DataSetSummaries']))]


#retrieving a list of the role ARNs as the owner of the data set id for the given aws account
data_set_permission_results = []
for i in range(len(data_set_ids)):
    data_set_permission_results.append(client.describe_data_set_permissions(
    AwsAccountId=acctid,
    DataSetId = data_sets['DataSetSummaries'][i]['DataSetId']
))

data_set_owners = [data_set_permission_results[i]['Permissions'][0]['Principal'] for i in range(len(data_set_permission_results))]


#set up dynamodb connection
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('qs_test')


#batch write items to dynamodb table with the following attributes: dataset id, dataset name, and dataset owner
with table.batch_writer() as batch:
    for i in range(len(data_set_ids)):
        batch.put_item(
            Item={
                'DataSetId': str(data_sets['DataSetSummaries'][i]['DataSetId']),
                'DataSetName': str(data_sets['DataSetSummaries'][i]['Name']),
                'DataSetOwner': str(data_set_permission_results[i]['Permissions'][0]['Principal'])
            }
    )
