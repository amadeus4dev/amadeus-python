from amadeus.client.decorator import Decorator


class CategoryRatedAreas(Decorator, object):
    def get(self, **params):
        '''
        Gets popularity score for location categories

        .. code-block:: python

            amadeus.location.analytics.category_rated_areas.get(
                            latitude=41.397158,
                            longitude=2.160873)

        :param latitude: latitude of geographic location to search around.
            For example: ``41.397158``
        :param longitude: longitude of geographic location to search around.
            For example: ``2.160873``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/location/analytics/category-rated-areas',
                               **params)
