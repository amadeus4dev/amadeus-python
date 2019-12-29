from amadeus.client.decorator import Decorator


class Seatmaps(Decorator, object):
    def get(self, **params):
        '''
        Allows you to retrieve the seat map of one or several flights.

        .. code-block:: python

            amadeus.shopping.seatmaps.get(
                flight-orderId='1577655015934--776131526'
            )

        :param flight-orderId: identifier of the order.
        Either a flight offer or a flight order Id.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/shopping/seatmaps', **params)

    def post(self, body):
        '''
        Allows you to retrieve the seat map of one or several flights.

        .. code-block:: python

            amadeus.shopping.seatmaps.post(body)

        :param body: the parameters to send to the API

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/shopping/seatmaps', body)
