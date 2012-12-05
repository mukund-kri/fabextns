from fabric.api import cd, run

from core import ServiceNotFound
from .base import BaseDBTasks


class MySQLServiceNotFound(Exception):
    pass

class MySQL(BaseDBTasks):
    
    def __init__(self):
        try:
            super(MySQL, self).__init__('mysql')
        except ServiceNotFound:
            raise MySQLServiceNotFound

    def dump_to_fs(self):
        super(MySQL, self).dump_to_fs()
        with cd(self.backup_folder):
            # First dump the db
            run('mysqldump --all-databases > mysqldump.sql')
            
            # Then nicely tar it up
            self._tarup_dump('mysqldump.sql')

            # Clean up every thing except the tared file
            run('rm -rf mysqldump.sql')

