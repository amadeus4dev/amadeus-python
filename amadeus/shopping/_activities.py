from amadeus.client.decorator import Decorator
from amadeus.shopping.activities._by_square \
    import BySquare


class Activities(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.by_square = BySquare(client)

    def get(self, **params):
        '''
        Returns activities for a given location

        .. code-block:: python


            client.shopping.activities.get(
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
            '/v1/shopping/activities', **params)
