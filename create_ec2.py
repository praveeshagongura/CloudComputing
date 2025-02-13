import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
instance = ec2.create_instances(
        ImageId='ami-085ad6ae776d8f09c',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='MyKeyPair',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyPythonEC2Instance'}
            ]
        }
    ]
)
print(f'Created instance with ID: {instance[0].id}')
