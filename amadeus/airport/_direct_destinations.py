from amadeus.client.decorator import Decorator


class DirectDestinations(Decorator, object):
    def get(self, **params):
        '''
        Returns airport direct routes.

        .. code-block:: python

            amadeus.airport.direct_destinations.get(
                            departureAirportCode='BLR')

        :param departureAirportCode: the departure Airport code following
            IATA standard. ``"BLR"``, for example for Bengaluru

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/airport/direct-destinations', **params)
