from amadeus.client.decorator import Decorator


class Upselling(Decorator, object):
    def post(self, body):
        '''
        Get flight offers with branded fares

        .. code-block:: python

            amadeus.shopping.flight_offers.upselling.post(body)

        :param body: the parameters to send to the API

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post(
            '/v1/shopping/flight-offers/upselling', body)
