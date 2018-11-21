from amadeus.client.decorator import Decorator


class FlightDates(Decorator, object):
    def get(self, **params):
        '''
        Find the cheapest flight dates from an origin to a destination.

        .. code-block:: python

            amadeus.shopping.flight_dates.get(origin='NYC', destination='MAD')

        :param origin: the City/Airport IATA code from which the flight will
            depart. ``"NYC"``, for example for New-York.

        :param destination: the City/Airport IATA code to which the flight is
            going. ``"MAD"``, for example for Madrid.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/shopping/flight-dates', **params)
