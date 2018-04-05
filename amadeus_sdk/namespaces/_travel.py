from amadeus_sdk.client.decorator import Decorator
from amadeus_sdk.travel._analytics import Analytics


class Travel(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
