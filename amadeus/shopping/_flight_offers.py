from amadeus.client.decorator import Decorator
from amadeus.shopping.flight_offers._prediction import FlightChoicePrediction


class FlightOffers(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.prediction = FlightChoicePrediction(client)

    def get(self, **params):
        '''
        Find the cheapest bookable flights.

        .. code-block:: python

            amadeus.shopping.flight_offers.get(
                origin='MAD',
                destination='NYC',
                departureDate='2019-08-01'
            )

        :param origin: the City/Airport IATA code from which the flight will
            depart. ``"MAD"``, for example for Madrid.

        :param destination: the City/Airport IATA code to which the flight is
            going. ``"BOS"``, for example for Boston.

        :param departureDate: the date on which to fly out, in `YYYY-MM-DD`
            format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/shopping/flight-offers', **params)
