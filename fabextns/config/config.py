import yaml
from fabric.api import env 
from voluptuous import Schema, Required

schema = Schema({
        Required('backup_folder'): str,
        Required('stage_folder'): str
        }, extra=True)


def load_cfg_to_env(filename='fab.yml'):

    config = yaml.load(file(filename))
    env.config = config
    schema(env.config)





    
