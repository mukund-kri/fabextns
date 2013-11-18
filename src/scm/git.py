from fabric.api import cd, run

from .base import FabRepo


class GitRepo(FabRepo):

    def __init__(self, reponame):
        super(GitRepo, self).__init__(reponame)

    def is_repo(self):
        self._attrs_not_exist("local_folder", "repo_name")

    def clone(self):
        self._attrs_not_exist("local_folder", "remote_url")
        run('mkdir -p %s' % self.local_folder)
        with cd(self.local_folder):
            cmd = "git clone %s" % self.remote_url
            run(cmd)
            
    def pull(self):
        self._attrs_not_exist("local_folder", "repo_name")
        lrepo = self.local_folder + '/' + self.repo_name
        with cd(lrepo):
            run('git pull')
        
                    
                
