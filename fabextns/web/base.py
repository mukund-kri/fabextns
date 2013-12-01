'''
  This is one way, our way and one of many ways of deploying python webapps. 
Here we copy source code from a folder where the latest code is present 
to the target folder where it is served with uWSGI, gunicorn etc. 
 Also many actions including backup, configuration etc. is done between 
these two steps.
''' 

from datetime import datetime
from fabric.api import run, env
from fabric.contrib.files import *


# config parameters required for any web app deployment


class BaseWebFab(object):
    
    def __init__(self, repo_name, path_in_repo):
        self.stage_folder = env.config['stage_folder']
        self.backup_folder = env.config['backup_folder']
        self.srv_folder = env.config['srv_folder']
        self.src_folder = os.path.join(self.stage_folder, repo_name, path_in_repo)

    def backup(self):
        dt_format = '%Y.%m.%d-%H.%M'
        bkp_target = '%s/bkp.%s' % (self.backup_folder, 
                                    datetime.now().strftime(dt_format))
        if exists(self.srv_folder):
            run('mv %s %s' % (self.srv_folder, bkp_target))
        
    def copy_code(self):
        run('mkdir -p %s' % self.srv_folder)
        run('cp -r %s/* %s' % (self.src_folder, self.srv_folder))

    def configure(self):
        pass

    def read_from_config(self):
        self.web_bkp_folder = "/tmp/web"

                                    
