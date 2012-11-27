from core.service import Service

class BaseDBTasks(Service):
    
    def __init__(self, name):
        super(BaseDBTasks, self).__init__(name)

    def dump_to_fs(self):
        pass

    def restore_from_fs(self):
        pass

    def cleanup_dbdumps(self):
        pass
