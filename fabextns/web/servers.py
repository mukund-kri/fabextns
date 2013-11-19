from core.service import Service


# This is very thin as only stop, start and restart is supported.
class ApacheFab(Service):
    def __init__(self):
        super(ApacheFab, self).__init__('apache'))
        

class NginxFab(Service):
    def __init__(self):
        super(NginxFab, self).__init__('nginx'))


