from amadeus.client.decorator import Decorator
from amadeus.safety._safety_rated_locations import SafetyRatedLocations
from amadeus.safety._safety_rated_location import SafetyRatedLocation


class Safety(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.safety_rated_locations = SafetyRatedLocations(client)

    def safety_rated_location(self, safety_id):
        return SafetyRatedLocation(self.client, safety_id)
