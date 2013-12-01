from fabric.api import cd, run
from fabric.contrib.files import *

from .base import BaseRepo

class MercurialRepo(BaseRepo):

    def __init__(self, name, url):
        super(MercurialRepo, self).__init__(name, url)
        

    def clone(self):
        
        run('mkdir -p %s' % self.stage_folder)
        with cd(self.stage_folder):
            cmd = "hg clone %s" % self.url
            run(cmd)

    def pull(self):
        lrepo = self.stage_folder + '/' + self.name
        if not exists(lrepo):
            self.clone()
        else:
            with cd(lrepo):
                run('hg pull && hg update')
            
