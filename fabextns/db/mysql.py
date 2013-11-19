import os

from fabric.api import cd, run, env
from voluptuous import Schema, Required

from fabextns.core import ServiceNotFound
from .base import BaseDBTasks


class MySQLServiceNotFound(Exception):
    pass


# config parameters required for mongo
schema = Schema({
        Required('mysql'):
            { Required('user'): str,
              Required('dbs'): list }
        }, extra=True)


class MySQL(BaseDBTasks):
    
    def __init__(self):
        try:
            super(MySQL, self).__init__('mysql')
        except ServiceNotFound:
            raise MySQLServiceNotFound
        schema(env.config)
        self.dbs = env.config['mysql']['dbs']
        self.user = env.config['mysql']['user']
        self.password = env.config['mysql']['password']

    def dump_to_fs(self):
        super(MySQL, self).dump_to_fs()

        run('mkdir -p %s/dbdump/mysqldump' % self.stage_folder)
        with cd(os.path.join(self.stage_folder, 'dbdump')):

            # First dump the db
            for db in self.dbs:
                if self.password:
                    run('mysqldump -u %s -p %s %s > mysqldump/%s.sql' %        \
                        (self.user, self.password, db, db))
                else:
                    run('mysqldump -u %s %s > mysqldump/%s.sql' %              \
                        (self.user, db, db))
            
            # Then nicely tar it up and move to dump folder
            dumpfile = self._tarup_dump('mysqldump')
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
            fls = run('ls mysqldump').split()
            for fl in fls:
                run('mysql < mysqldump/%s' % (fl))
        run('rm -rf %s' % temp_folder)
