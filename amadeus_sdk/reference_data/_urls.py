from amadeus_sdk.client.decorator import Decorator
from amadeus_sdk.reference_data.urls._checkin_links import CheckinLinks


class Urls(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.checkin_links = CheckinLinks(client)
