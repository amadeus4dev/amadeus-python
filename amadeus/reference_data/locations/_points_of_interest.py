from amadeus.client.decorator import Decorator
from amadeus.reference_data.locations.points_of_interest._by_square \
    import BySquare


class PointsOfInterest(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.by_square = BySquare(client)

    def get(self, **params):
        '''
        Returns a list of relevant point of interests near to a given point.

        .. code-block:: python


            client.reference_data.locations.points_of_interest.get(
                longitude=2.160873,
                latitude=41.397158
            )

        :param latitude: latitude of geographic location to search around.
            For example: ``41.397158``
        :param longitude: longitude of geographic location to search around.
            For example: ``2.160873``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/locations/pois', **params)
