from .base import BaseWebFab


class FlaskFab(BaseWebFab):

    def deploy(self):
        self.backup()
        self.copy_code()
