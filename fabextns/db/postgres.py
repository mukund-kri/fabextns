import os

from fabric.api import cd, run, env
from voluptuous import Schema, Required

from fabextns.core import ServiceNotFound
from .base import BaseDBTasks


class PostgresServiceNotFound(Exception):
    pass


# config parameters required for mongo
schema = Schema({
        Required('postgres'):
            { Required('user'): str,
              Required('dbs'): list }
        }, extra=True)


class Postgres(BaseDBTasks):
    
    def __init__(self):
        try:
            super(Postgres, self).__init__('postgresql')
        except ServiceNotFound:
            raise PostgresServiceNotFound
        schema(env.config)
        self.dbs = env.config['postgres']['dbs']
        self.user = env.config['postgres']['user']
        self.password = env.config['postgres']['password']

    def dump_to_fs(self):
        super(Postgres, self).dump_to_fs()

        run('mkdir -p %s/dbdump/postgresdump' % self.stage_folder)
        with cd(os.path.join(self.stage_folder, 'dbdump')):

            # First dump the db. Assuming the user has a .pgpass file
            for db in self.dbs:
                run('pg_dump %s > postgresdump/%s.sql' %                       \
                        (db, db))
            
            # Then nicely tar it up and move to dump folder
            dumpfile = self._tarup_dump('postgresdump')
            run('mv %s %s' % (dumpfile, self.backup_folder))
        
        # Clean up every thing
        run('rm -rf  %s' % (os.path.join(self.stage_folder, 'dbdump')))
            
    def restore_from_tar(self, tar_file, location=None, delete=True):
        if not location:
            location = self.backup_folder
        tar_path = os.path.join(location, tar_file)
        # make a temp directory to unzip and restore db
        temp_folder = '%s/dbrestore' % self.stage_folder
        run('mkdir -p %s' % temp_folder)
        with cd(temp_folder):
            run('tar -xjvf %s' % tar_path)
            fls = run('ls postgresdump').split()
            for fl in fls:
                db = fl.split(".")[0]
                run('psql %s < postgresdump/%s' % (db, fl))
        run('rm -rf %s' % temp_folder)
