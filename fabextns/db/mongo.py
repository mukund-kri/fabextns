import os

from fabric.api import cd, run, env
from voluptuous import Schema, Required

from fabextns.core import ServiceNotFound
from .base import BaseDBTasks


class MongoServiceNotFound(Exception):
    pass


# for validating if the config file has all the parameters mongo needs
schema = Schema({
        Required('mongo'):
            {Required('dbs'): list}
        }, extra=True)

class MongoDB(BaseDBTasks):
    
    def __init__(self):
        try:
            super(MongoDB, self).__init__('mongodb')
        except ServiceNotFound:
            raise MongoServiceNotFound()
        schema(env.config)           # validate if we config has all data
        self.dbs = env.config['mongo']['dbs']
        
    def dump_to_fs(self):
        super(MongoDB, self).dump_to_fs()
        tarfile = ""
        with cd(self.backup_folder):
            # First dump the dbs
            for db in self.dbs:
                run('mongodump --db %s' % db)
            
            # Then nicely tar it up
            tarfile = self._tarup_dump('dump')

            # Clean up every thing except the tared file
            run('rm -rf dump')
        return tarfile

    def restore_from_tar(self, tar_file, location=None, delete=True):
        if not location:
            location = self.backup_folder
        tar_path = os.path.join(location, tar_file)
        
        # make a temp directory to unzip and restore db
        temp_folder = '%s/dbrestore' % self.stage_folder
        run('mkdir -p %s' % temp_folder)
        with cd(temp_folder):
            run('tar -xjvf %s' % tar_path)
            run('mongorestore --drop')
        run('rm -rf %s' % temp_folder)           # cleanup
 
            

