from amadeus.client.decorator import Decorator


class Airports(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of relevant airports near to a given point.

        .. code-block:: python


            amadeus.reference_data.locations.airports.get(
                longitude=49.0000,
                latitude=2.55
            )

        :param latitude: latitude of geographic location to search around.
            For example: ``52.5238``
        :param longitude: longitude of geographic location to search around.
            For example: ``13.3835``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/locations/airports', **params)
