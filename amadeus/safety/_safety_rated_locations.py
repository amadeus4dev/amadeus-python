from amadeus.client.decorator import Decorator
from amadeus.safety.safety_rated_locations._by_square import BySquare


class SafetyRatedLocations(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.by_square = BySquare(client)

    def get(self, **params):
        '''
        Returns the overall safety ranking and a detailed safety
            ranking of all the districts within the given radius.

        .. code-block:: python


            amadeus.safety.safety_rated_locations.get(
                longitude=2.160873,
                latitude=41.397158
            )

        :param latitude: latitude of the location to safety ranking search.
            For example: ``41.397158``
        :param longitude: longitude of the location to safety ranking search.
            For example: ``2.160873``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/safety/safety-rated-locations', **params)
