from amadeus.client.decorator import Decorator


class FlightChoicePrediction(Decorator, object):
    def post(self, body):
        '''
        Forecast traveler choices in the context of search & shopping.

        .. code-block:: python

            amadeus.shopping.flight_offers.prediction.post(
                amadeus.shopping.flight_offers_search.get(
                originLocationCode='SYD',
                destinationLocationCode='BKK',
                departureDate='2020-11-01',
                adults=1).result
        )

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v2/shopping/flight-offers/prediction', body)
