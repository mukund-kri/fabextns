from fabric.api import env

from fabextns.db import MongoDB, MongoServiceNotFound
from fabextns.db import MySQL, MySQLServiceNotFound
from fabextns.config import load_cfg_to_env

env.hosts = ['localhost']
env.user = 'deploy'
env.password = 'deploy'


# load all our custom values to env
load_cfg_to_env()
dump_tar = 'mysqldump.2013.11.19-15.23.tar.bz'


def test_mongo():
    try:
        mongo = MongoDB()
        mongo.status()
        mongo.stop()
        mongo.start()
        dump_name = mongo.dump_to_fs()
        # mongo.restore_from_tar(dump_tar)
        mongo.cleanup_dbdumps()
    
    except MongoServiceNotFound:
        print(red("Could not find the Mongo serice. Perhaps not installed?"))
        
        
def test_mysql():
    mysql = MySQL()
    # mysql.status()
    # mysql.stop()
    # mysql.start()

    dump_name = mysql.dump_to_fs()
    # mysql.cleanup_dbdumps()
    mysql.restore_from_tar(dump_tar)


def test():
    test_mysql()


