from datetime import datetime

from fabric.api import env, run
from fabric.context_managers import cd

from core.service import Service


class BackupFolderNotDefined(Exception):
    pass


class BaseDBTasks(Service):
    
    def __init__(self, name):
        super(BaseDBTasks, self).__init__(name)
        
        self.backup_folder = env.get('BACKUP_FOLDER', '/tmp/bkp')
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
        raise NotImplementedError()

    def cleanup_dbdumps(self, keep_last=5):
        # To implement. Write code to list out dbdump dir, filtered by the
        # dump file syntax.
        with cd(self.backup_folder):
            backups = run('ls -t')
            backups = backups.split()
            if len(backups) > keep_last:
                # get all the backups other than last n backups
                to_delete = backups[keep_last:]
                for bkp in to_delete:
                    run('rm -rf %s' % bkp)


    def _tarup_dump(self, dumpfile):
        dt_format = '%Y.%m.%d-%H.%M'
        tarfile = 'dump.%s.tar.bz' % datetime.now().strftime(dt_format)
        run('tar -cjvf %s %s' % (tarfile, dumpfile))
