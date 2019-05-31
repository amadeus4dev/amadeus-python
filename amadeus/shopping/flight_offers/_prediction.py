from amadeus.client.decorator import Decorator


class FlightChoicePrediction(Decorator, object):
    def post(self, body):
        '''
        Forecast traveler choices in the context of search & shopping.

        .. code-block:: python

            amadeus.shopping.flight_offers.prediction.post(
                amadeus.shopping.flight_offers.get(origin='MAD',
                destination='NYC',
                departureDate='2019-08-01'
            ).body
        )

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/shopping/flight-offers/prediction', body)
