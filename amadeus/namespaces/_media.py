from amadeus.client.decorator import Decorator
from amadeus.media._files import Files


class Media(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.files = Files(client)
