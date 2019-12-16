from amadeus.client.decorator import Decorator
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class FlightOffersPrice(Decorator, object):
    def post(self, flightoffers, **params):
        '''
        Gets a confirmed price and availability of a flight

        .. code-block:: python

            amadeus.shopping.flight_offers.pricing.post(body, params)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        url = '/v1/shopping/flight-offers/pricing'

        if params is not None:
            url = '/v1/shopping/flight-offers/pricing?'

        body = {'data': {'type': 'flight-offers-pricing',
                'flightOffers': list(flightoffers)}}

        return self.client.post((url + urlencode(params)), body)
