from configobj import ConfigObj
from fabric.api import env 


def config_to_env(filename='fab.cfg'):

    config = ConfigObj(filename)
    db_cfg = config['db']
    env['BACKUP_FOLDER'] = db_cfg.get('backup.folder')

    
