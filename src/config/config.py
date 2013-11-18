import yaml
from fabric.api import env 


def config_to_env(filename='fab.yml'):

    config = yaml.load(file(filename))
    print config
    env['BACKUP_FOLDER'] = config.get('backup_folder', '/tmp/bkp')

    
