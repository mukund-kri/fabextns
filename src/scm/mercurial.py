from fabric.api import cd, run
from fabric.contrib.files import *

from .base import FabRepo

class MercurialRepo(FabRepo):

    def __init__(self, reponame):
        super(MercurialRepo, self).__init__(reponame)

    def clone(self):
        run('mkdir -p %s' % self.local_folder)
        with cd(self.local_folder):
            cmd = "hg clone %s" % self.remote_url
            run(cmd)

    def pull(self):
        lrepo = self.local_folder + '/' + self.repo_name
        if not exists(lrepo):
            self.clone()
        else:
            with cd(lrepo):
                run('hg pull && hg update')
            
