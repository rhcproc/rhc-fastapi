"""
# DynamonDB 관련 문서
https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
"""
import boto3
# from config import config
from settings import settings

def get_cursor(uri: str = None):
    if uri:
        return boto3.resource(
            'dynamodb',
            endpoint_url=uri
        )
    return boto3.resource(
        'dynamodb',
        aws_access_key_id=settings.DYNAMODB_ACCESS_KEY,
        aws_secret_access_key=settings.DYNAMODB_SECRET_KEY,
        region_name=settings.DYNAMODB_REGION
    )

# Models Shorts
from model.dynamodb.state import State