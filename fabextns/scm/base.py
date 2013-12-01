from fabric.api import cd, run, env
from voluptuous import Schema, Required


schema = Schema({
        Required('stage_folder'): str,
        Required('srv_folder'): str,
        Required('backup_folder'): str,
        }, extra=True)

class BaseRepo(object):

    def __init__(self, name, url):
        schema(env.config)
        self.name = name
        self.url = url

        self.stage_folder = env.config['stage_folder']
        self.srv_folder = env.config['srv_folder']
        self.backup_folder = env.config['backup_folder']

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
        
                    
                
