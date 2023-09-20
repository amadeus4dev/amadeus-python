from amadeus.client.decorator import Decorator


class ByHotels(Decorator, object):
    def get(self, **params):
        '''
        Searches for hotel using it's unique id.

        .. code-block:: python


            amadeus.reference_data.locations.hotels.by_hotels.get(
                hotelIds=["ADPAR001"])

        :param hotelIds: Amadeus Property Codes (8 chars)
            For example: ``["ADPAR001"]``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        for key, value in params.items():
            if isinstance(value, list):
                params[key] = ','.join(value)
        return self.client.get(
            '/v1/reference-data/locations/hotels/by-hotels', **params)
