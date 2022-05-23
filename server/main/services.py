from django.conf import settings
from pymongo import MongoClient


class TestResultService:
    """
    Данный класс реализует логику для расчёта и хранения результатов тестирования в MongoDB.
    """

    def __init__(self, some_id: int):
        self.client = MongoClient(host=settings.MONGODB_HOST,
                                  port=settings.MONGODB_PORT,
                                  username=settings.MONGODB_USERNAME,
                                  password=settings.MONGODB_PASSWORD)
        self.collection = self.client[settings.MONGODB_DATABASE]['count_views']
        self.product_id = some_id
