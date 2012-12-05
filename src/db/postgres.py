from fabric.api import cd, run, sudo

from core import ServiceNotFound
from .base import BaseDBTasks

class PostgresServiceNotFound(Exception):
    pass

class PostgresFab(BaseDBTasks):
    
    def __init__(self):
        try:
            super(PostgresFab, self).__init__('postgresql')
        except ServiceNotFound:
            raise PostgresServiceNotFound

    def dump_to_fs(self):
        # TODO: Take care of permissions. Right now this assumes sudo 
        # access and a db super user called postgres.
        super(PostgresFab, self).dump_to_fs()

        with cd(self.backup_folder):
            # First dump the db
            sudo('pg_dump -U postgres -h localhost > pg.dump.sql')
            
            # Then nicely tar it up
            self._tarup_dump('pg.dump.sql')

            # Clean up every thing except the tared file
            run('rm -rf pg.dump.sql')
