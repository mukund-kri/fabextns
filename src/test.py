from db import MongoDB, MongoServiceNotFound
from core import *

def test():

    try:
        mongo = MongoDB()
        mongo.status()
        mongo.stop()
        mongo.start()
    
    except MongoServiceNotFound:
        print(red("Could not find the Mongo serice. Perhaps not installed?"))
