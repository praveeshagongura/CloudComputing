import boto3

# List all files in an S3 bucket
def list_s3_files(bucket_name):
    s3 = boto3.client('s3')
    print(f"Files in S3 bucket '{bucket_name}':")
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print("Bucket is empty or does not exist.")

# Create a DynamoDB table with a waiter
def create_dynamodb_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'UserID', 'KeyType': 'HASH'},
                {'AttributeName': 'Timestamp', 'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'UserID', 'AttributeType': 'S'},
                {'AttributeName': 'Timestamp', 'AttributeType': 'N'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"DynamoDB table '{table_name}' created. Waiting until it becomes ACTIVE...")

        # Wait until the table is ACTIVE
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        print("Table is now ACTIVE.")

    except dynamodb.exceptions.ResourceInUseException:
        print(f"Table '{table_name}' already exists.")

# Insert item into DynamoDB table
def insert_item(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item={
                'UserID': {'S': 'user123'},
                'Timestamp': {'N': '1713849000'},
                'Name': {'S': 'Praveesha'},
                'Email': {'S': 'praveesha@example.com'},
                'LastLogin': {'S': '2025-04-23T00:00:00Z'}
            }
        )
        print("Item inserted into DynamoDB table.")
    except dynamodb.exceptions.ResourceNotFoundException:
        print("Table not found. Did you wait until it became active?")

# Run all steps
if __name__ == "__main__":
    bucket_name = 'cf-homework3-bucket-626635413797'
    table_name = 'HW3UsersTable'

    list_s3_files(bucket_name)
    create_dynamodb_table(table_name)
    insert_item(table_name)
