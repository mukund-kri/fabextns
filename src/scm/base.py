from configobj import ConfigObj
from fabric.api import cd, run

class ConfigNotDefinedError(Exception):
    
    def __init__(self, message=""):
        Exception.__init__(self, message)

class FabRepo(object):

    def __init__(self, reponame):
        self.reponame = reponame

    def is_repo(self):
        raise NotImplementedError

    def clone(self):
        raise NotImplementedError
            
    def pull_or_update(self):
        raise NotImplementedError
            
    def delete(self):
        self._attrs_not_exist("local_folder", "repo_name")
        lrepo = self.local_folder + "/" + self.repo_name
        run("rm -rf %s" % lrepo)
                
    def _attrs_not_exist(self, *attrs):
        existance = map(lambda attr: hasattr(self, attr), attrs)
        if not reduce(lambda x, y: x and y, existance):
            attrs_str = ", ".join(attrs)
            raise ConfigNotDefinedError("One of these attrs not defined: %s"  % attrs_str)
        
                    
                
