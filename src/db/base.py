from datetime import datetime

from core.service import Service
from fabric.api import env, run

class BackupFolderNotDefined(Exception):
    pass


class BaseDBTasks(Service):
    
    def __init__(self, name):
        super(BaseDBTasks, self).__init__(name)
        
        self.backup_folder = env.get('BACKUP_FOLDER', None)
        if self.backup_folder:
            run('mkdir -p %s' % self.backup_folder)
        
    def dump_to_fs(self):
        if self.backup_folder:
            run('mkdir -p %s' % self.backup_folder)
        else:
            print("Backup folder not defined in config")
            raise BackupFolderNotDefined

    def restore_from_fs(self):
        # Select the dump to restore from. Delete the db/s then restore from
        # dump. This is db specific so it should be in the derived class. Not
        # here.
        pass

    def cleanup_dbdumps(self):
        # To implement. Write code to list out dbdump dir, filtered by the
        # dump file syntax.
        pass

    def _tarup_dump(self, dumpfile):
        dt_format = '%Y.%m.%d-%H.%M'
        tarfile = 'dump.%s.tar.bz' % datetime.now().strftime(dt_format)
        run('tar -cjvf %s %s' % (tarfile, dumpfile))
