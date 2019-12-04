from amadeus.client.decorator import Decorator


class FlightOffersPrice(Decorator, object):
    def post(self, body):
        '''
        Gets a confirmed price and availability of a flight

        .. code-block:: python

            amadeus.shopping.flight_offers.pricing.post(body)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/shopping/flight-offers/pricing', body)
