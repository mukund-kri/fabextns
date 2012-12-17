from .base import BaseWebFab

class DjangoFab(BaseWebFab):

    def deploy(self):
        self.backup()
        self.copy_code()




                                    
