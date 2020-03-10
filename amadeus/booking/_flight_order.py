from amadeus.client.decorator import Decorator


class FlightOrder(Decorator, object):
    def __init__(self, client, flight_order_id):
        Decorator.__init__(self, client)
        self.flight_order_id = flight_order_id

    def get(self, **params):
        '''
        Retrieves a flight order based on its ID.

        .. code-block:: python

            amadeus.booking.flight_order('eJzTd9f3NjIJdzUGAAp%2fAiY=').get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/booking/flight-orders/{0}'
                               .format(self.flight_order_id), **params)

    def delete(self, **params):
        '''
        Deletes a flight order based on its ID.

        .. code-block:: python

            amadeus.booking.flight_order('eJzTd9f3NjIJdzUGAAp%2fAiY=').delete()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.delete('/v1/booking/flight-orders/{0}'
                                  .format(self.flight_order_id), **params)
