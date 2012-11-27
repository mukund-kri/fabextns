from core import ServiceNotFound
from .base import BaseDBTasks

class MongoServiceNotFound(Exception):
    pass

class MongoDB(BaseDBTasks):
    
    def __init__(self):
        try:
            super(MongoDB, self).__init__('mongodb')
        except ServiceNotFound:
            raise MongoServiceNotFound
