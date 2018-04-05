from amadeus.client.decorator import Decorator


class FlightOffers(Decorator, object):
    def get(self, **params):
        '''
        Find the cheapest bookable flights.

        .. code-block:: python

            amadeus.shopping.flight_destinations.get(
                origin='LHR',
                destination='PAR',
                departureDate='2017-12-24'
            )

        :param origin: the City/Airport IATA code from which the flight will
            depart. ``"BOS"``, for example for Boston.

        :param destination: the City/Airport IATA code to which the flight is
            going. ``"BOS"``, for example for Boston.

        :param departureDate: the date on which to fly out, in `YYYY-MM-DD`
            format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/shopping/flight-offers', **params)
