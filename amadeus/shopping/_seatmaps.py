from amadeus.client.decorator import Decorator


class Seatmaps(Decorator, object):
    def get(self, **params):
        '''
        Allows you to retrieve the seat map of one or several flights based
        on the flight-orderId returned from Flight Create Orders API Call.

        .. code-block:: python

            amadeus.shopping.seatmaps.get(
                flight-orderId='<order_id>'
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
        Take the body of a flight offer search or flight offer price
        and pass it in to this method to get a seatmap

        .. code-block:: python

            amadeus.shopping.seatmaps.post(body)

        :param body: the parameters to send to the API

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/shopping/seatmaps', body)
