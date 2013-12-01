from fabric.api import env

from fabextns.db import MongoDB, MongoServiceNotFound
from fabextns.db import MySQL, MySQLServiceNotFound
from fabextns.db import Postgres, PostgresServiceNotFound
from fabextns.config import load_cfg_to_env


env.hosts = ['localhost']
env.user = 'deploy'
env.password = 'deploy'


# load all our custom values to env
load_cfg_to_env()
dump_tar = 'postgresdump.2013.11.26-19.29.tar.bz'


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

def test_postgres():
    postgres = Postgres()
    # postgres.status()
    # postgres.stop()
    # postgres.start()

    dump_name = postgres.dump_to_fs()
    postgres.cleanup_dbdumps()
    # postgres.restore_from_tar(dump_tar)


def test():
    test_postgres()


from fabextns.scm import MercurialRepo
from fabextns.web import FlaskFab
from fabextns.core import Service

def deploy_flask():
    
    '''
    repo = MercurialRepo(
        'flask-skel',
        'ssh://hg@bitbucket.org/mukund_kri/flask-skel')
    
    repo.pull()

    flask = FlaskFab(
        repo_name='flask-skel',
        path_in_repo='trunk/flask-mongo',
        )
    flask.backup()
    flask.copy_code()
    '''

    usgi = Service('flaskuwsgi')
    usgi.restart()

    nginx = Service('nginx')
    nginx.restart()
