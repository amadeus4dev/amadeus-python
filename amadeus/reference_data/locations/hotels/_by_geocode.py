from amadeus.client.decorator import Decorator


class ByGeocode(Decorator, object):
    def get(self, **params):
        '''
        Searches for hotel using a geocode.

        .. code-block:: python


            amadeus.reference_data.locations.hotels.by_geocode.get(
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
            '/v1/reference-data/locations/hotels/by-geocode', **params)
