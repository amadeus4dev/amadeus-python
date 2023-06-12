from amadeus.client.decorator import Decorator

from urllib.parse import urlencode


class Cancellation(Decorator, object):
    def __init__(self, client, order_id):
        Decorator.__init__(self, client)
        self.order_id = order_id

    def post(self, body, **params):
        '''
        Cancels a transfer reservation

        .. code-block:: python

            amadeus.ordering.transfer_order(order_id).transfers.cancellation.post(body,
            confirmNbr=confirm_nbr)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        url = '/v1/ordering/transfer-orders/{0}/transfers/cancellation?'.format(
            self.order_id
        )
        return self.client.post(url + urlencode(params), body)
