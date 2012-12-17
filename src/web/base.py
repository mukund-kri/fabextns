'''
  This is one way, our way and one of many ways of deploying python webapps. 
Here we copy source code from a folder where the latest code is present 
to the target folder where it is served with uWSGI, gunicorn etc. 
 Also many actions including backup, configuration etc. is done between 
these two steps.
''' 

from datetime import datetime
from fabric.api import run

class BaseWebFab(object):
    
    def __init__(self, src_folder, srv_folder):
        self.src_folder = src_folder
        self.srv_folder = srv_folder

        self.read_from_config()
        self.configure()

    def backup(self):
        dt_format = '%Y.%m.%d-%H.%M'
        bkp_target = '%s/bkp.%s' % (self.web_bkp_folder, 
                                    datetime.now().strftime(dt_format))
        run('mv %s %s' % (self.srv_folder, bkp_target))
        
    def copy_code(self):
        run('cp -r %s %s' % (self.src_folder, self.srv_folder))

    def configure(self):
        pass

    def read_from_config(self):
        self.web_bkp_folder = "/tmp/web"

                                    
