from amadeus_sdk.client.decorator import Decorator
from amadeus_sdk.reference_data._urls import Urls
from amadeus_sdk.reference_data._location import Location
from amadeus_sdk.reference_data._locations import Locations


class ReferenceData(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.urls = Urls(client)
        self.locations = Locations(client)

    def location(self, location_id):
        return Location(self.client, location_id)
