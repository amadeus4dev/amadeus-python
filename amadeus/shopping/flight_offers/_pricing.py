from amadeus.client.decorator import Decorator
try:
    from urllib.parse import urlencode
except ImportError:     # pragma: no cover
    from urllib import urlencode    # pragma: no cover


class FlightOffersPrice(Decorator, object):
    def post(self, body, **params):
        '''
        Gets a confirmed price and availability of a flight

        .. code-block:: python

            amadeus.shopping.flight_offers.pricing.post(body, params)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        url = '/v1/shopping/flight-offers/pricing?'
        flight_offers = []
        if type(body) is not list:
            flight_offers.append(body)
        else:
            flight_offers.extend(body)
        return self.client.post(url + urlencode(params),
                                {'data':
                                {'type': 'flight-offers-pricing',
                                    'flightOffers': flight_offers}})
