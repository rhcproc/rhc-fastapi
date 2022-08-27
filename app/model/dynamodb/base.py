"""
Table: *-state
"""
from abc import ABCMeta
from decimal import Decimal
from functools import wraps
# from flask import current_app
from botocore.exceptions import ClientError
# from controller.util import app_is_running, remove_decimals
# from controller import log
from model.dynamodb import get_cursor


class Model(metaclass=ABCMeta):

    PARTITION_KEY = None
    TABLE_NAME = None
    VERSION = 1

    def __init__(self, db=None):
        # Flask가 실행중일 경우, 앱에서 가져옴
        # if db is None and app_is_running():
            # db = current_app.dynamodb
        # 아닐 경우, 직접 커서 함수를 실행하여 가져옴
        if db is None:
            db = get_cursor()

        # Validate Params
        if self.TABLE_NAME is None:
            raise NotImplementedError(
                'TABLE_NAME required.')
        if self.PARTITION_KEY is None:
            raise NotImplementedError(
                'PARTITION_KEY required.')

        self.table = db.Table(self.TABLE_NAME)

    @property
    def schema(self) -> dict:
        """Get default item format"""
        return {
            # Partition Key
            "id": None,
            # Item Version
            "__version__": self.VERSION,
        }

    def schemize(self, item: dict) -> dict:
        """Generate & Validate JSON scheme"""
        result = {**self.schema, **item}
        if not result.get(self.PARTITION_KEY):
            raise RuntimeError(f'No Partition Key: {self.PARTITION_KEY}')
        return result

    def put_item(self, item: dict):
        return self.table.put_item(
            Item=self.schemize(item)
        )

    def get_item(self, partition_key):
        try:
            res = self.table.get_item(
                Key={self.PARTITION_KEY: partition_key}
            )
        except ClientError as e:
            raise e
        return res.get('Item')

    def delete_item(self, partition_key):
        return self.table.delete_item(
            Key={self.PARTITION_KEY: partition_key}
        )