import boto3

ecr_client = boto3.client('ecr')  # Fix: ecr.client changed to ecr_client

repository_name = "my-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)  # Fix: using ecr_client

repository_uri = response['repository']['repositoryUri']

print(repository_uri)
