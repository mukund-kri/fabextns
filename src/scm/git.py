from configobj import ConfigObj
from fabric.api import cd, run


def config_to_env(reponame, filename='fab.cfg'):

    config = ConfigObj(filename)
    return config['repos'][reponame]


class GitRepo(object):

    def __init__(self, reponame):
        config = config_to_env(reponame)
        self.local_folder = config.get('local_folder')
        self.remote_url = config.get('remote_url')
        self.repo_name = config.get('repo_name')

    def clone(self):
        with cd(self.local_folder):
            cmd = "git clone %s" % self.remote_url
            run(cmd)

    def pull(self):
        lrepo = self.local_folder + '/' + self.repo_name
        with cd(lrepo):
            run('git pull')

    def delete(self):
        lrepo = self.local_folder + "/" + self.repo_name
        run("rm -rf %s" % lrepo)
