from amadeus.client.decorator import Decorator
from amadeus.reference_data.locations.hotels import ByCity
from amadeus.reference_data.locations.hotels import ByGeocode
from amadeus.reference_data.locations.hotels import ByHotels


class Hotels(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.by_hotels = ByHotels(client)
        self.by_geocode = ByGeocode(client)
        self.by_city = ByCity(client)
