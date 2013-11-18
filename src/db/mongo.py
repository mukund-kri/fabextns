from fabric.api import cd, run

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

    def dump_to_fs(self):
        super(MongoDB, self).dump_to_fs()

        with cd(self.backup_folder):
            # First dump the db
            run('mongodump')
            
            # Then nicely tar it up
            self._tarup_dump('dump')

            # Clean up every thing except the tared file
            run('rm -rf dump')
