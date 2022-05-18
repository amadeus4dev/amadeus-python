from amadeus.client.decorator import Decorator


class ByCity(Decorator, object):
    def get(self, **params):
        '''
        Searches for hotel in a given city.

        .. code-block:: python


            amadeus.reference_data.locations.hotels.by_city.get(
                cityCode='PAR')

        :param cityCode: the City IATA code for which to find a hotel, for
            example ``"PAR"`` for Paris.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/locations/hotels/by-city', **params)
