from amadeus.client.decorator import Decorator
from ._reference_data.urls import Urls
from ._reference_data.location import Location
from ._reference_data.locations import Locations


class ReferenceData(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.urls = Urls(client)
        self.locations = Locations(client)

    def location(self, location_id):
        return Location(self.client, location_id)
