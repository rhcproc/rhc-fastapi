import json
from model.dynamodb.base import Model
from handlers.utils import now2str
from settings import settings

class State(Model):
    TABLE_NAME = settings.DYNAMODB_STATE
    PARTITION_KEY = 'email'

    @property
    def schema(self) -> dict:
        return {
        'email': None, # PK
        'created_at': now2str(),
    }

    def put_body(self, state: str):
        """
        Insert
        - 이미 있을 경우, 덮어씌워버림
        """
        item = {'email': state}
        return self.put_item(item)

    def update_metadata(self, state: str, metadata: dict):
        return self.table.update_item(
            Key={'email': state},
            UpdateExpression="set metadata=:m",
            ExpressionAttributeValues={':m': metadata}
        )


if __name__ == '__main__':
    model = State()
    model.put_body(
        state='1aa@aa.com'
    )
    res = model.get_item('1')
    print(res)