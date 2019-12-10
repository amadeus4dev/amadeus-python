from amadeus.client.decorator import Decorator
from amadeus.shopping.flight_offers._prediction import FlightChoicePrediction


class FlightOffersSearch(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.prediction = FlightChoicePrediction(client)

    def get(self, **params):
        '''
        Get the cheapest flights on given journey

        .. code-block:: python

            amadeus.shopping.flight_offers_search.get(
                origin='MAD',
                destination='NYC',
                departureDate='2019-08-01',
                adults='1'
            )

        :param origin: the City/Airport IATA code from which the flight will
            depart. ``"MAD"``, for example for Madrid.

        :param destination: the City/Airport IATA code to which the flight is
            going. ``"BOS"``, for example for Boston.

        :param departureDate: the date on which to fly out, in `YYYY-MM-DD`
            format

        :param adults: the number of adult passengers with age 12 or older

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/shopping/flight-offers', **params)

    def post(self, body):
        '''
        Forecast traveler choices in the context of search & shopping.

        .. code-block:: python

            amadeus.shopping.flight_offers_search.post(body)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v2/shopping/flight-offers', body)
