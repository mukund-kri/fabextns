from fabric.api import *
from fabric.colors import green, red
from StringIO import StringIO
import re

env.host = ['localhost']
env.password = 'mukund'


class ServiceNotFound(Exception):
    pass


class Service(object):
    
    def __init__(self, name):
    
        output = StringIO
        with settings(warn_only=True):
            resp = sudo("service %s status" % name)
            if re.search("unrecognized service", resp):
                raise ServiceNotFound

        self.name = name

    def status(self):
        status = sudo("service %s status" % self.name)
        print(green(status))
        print('\n')

    def stop(self):
        with settings(warn_only=True):
            sudo("service %s stop" % self.name)

    def start(self):
        with settings(warn_only=True):
            sudo("service %s start" % self.name)




