from amadeus.client.decorator import Decorator


class FlightOrders(Decorator, object):
    def post(self, body):
        '''
        Books a flight

        .. code-block:: python

            amadeus.booking.flight_orders.post(body)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v1/booking/flight-orders', body)
