from db import MongoDB, MongoServiceNotFound
from db import MySQL, MySQLServiceNotFound
from db import PostgresFab, PostgresServiceNotFound

from config import config_to_env
from core import *


def test_mongo():
    try:
        mongo = MongoDB()
        # mongo.status()
        # mongo.stop()
        # mongo.start()
        mongo.dump_to_fs()
    
    except MongoServiceNotFound:
        print(red("Could not find the Mongo serice. Perhaps not installed?"))
        
        
def test_mysql():
    try:
        mysql = MySQL()
        # mysql.status()
        # mysql.stop()
        mysql.dump_to_fs()
    except MySQLServiceNotFound:
        print("not found")


def test_postgres():
    try:
        postgres = PostgresFab()
        # postgres.status()
        # postgres.stop()
        # postgres.start()
        postgres.dump_to_fs()
    except PostgresServiceNotFound:
        print("Not Found")


from scm import GitRepo, MercurialRepo

def test():
    config_to_env()

    # test_mongo()
    # test_mysql()
    #test_postgres()


    # git = GitRepo("LearnStreet")
    # git.is_repo()
    # git.clone()
    # git.pull()
    # git.delete()


    hg = MercurialRepo("Repo2")
    hg.clone()
    hg.pull()
    hg.delete()



