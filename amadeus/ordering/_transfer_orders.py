from amadeus.client.decorator import Decorator

from urllib.parse import urlencode


class TransferOrders(Decorator, object):
    def post(self, body, **params):
        '''
        Performs the final booking for a chosen transfer

        .. code-block:: python

            amadeus.ordering.transfer_orders.post(body, offerId=offer_id)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        url = '/v1/ordering/transfer-orders?'
        return self.client.post(url + urlencode(params), body)
