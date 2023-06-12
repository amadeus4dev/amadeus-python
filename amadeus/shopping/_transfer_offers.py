from amadeus.client.decorator import Decorator


class TransferOffers(Decorator, object):
    def post(self, body):
        '''
        Get transfer offers

        .. code-block:: python

            amadeus.shopping.transfer_offers.post(body)

        :param body: the parameters to send to the API

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/shopping/transfer-offers', body)
