from amadeus.client.decorator import Decorator


class FlightDestinations(Decorator, object):
    def get(self, **params):
        '''
        Find the cheapest destinations where you can fly to.

        .. code-block:: python

            amadeus.shopping.flight_destinations.get(origin='LON')

        :param origin: the City/Airport IATA code from which the flight will
            depart. ``"LON"``, for example for London.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''

        return self.client.get('/v1/shopping/flight-destinations', **params)
