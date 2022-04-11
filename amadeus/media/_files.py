from amadeus.client.decorator import Decorator


class Files(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
