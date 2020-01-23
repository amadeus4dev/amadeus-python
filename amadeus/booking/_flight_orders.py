from amadeus.client.decorator import Decorator


class FlightOrders(Decorator, object):
    def post(self, flight, travelers):
        '''
        Books a flight

        .. code-block:: python

            amadeus.booking.flight_orders.post(flight, travelers)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        flight_offers = []
        if type(flight) is not list:
            flight_offers.append(flight)
        else:
            flight_offers.extend(flight)  # pragma: no cover
        travelers_info = []
        if type(travelers) is not list:
            travelers_info.append(travelers)
        else:
            travelers_info.extend(travelers)  # pragma: no cover
        body = {'data': {'type': 'flight-order', 'flightOffers': flight_offers,
                         'travelers': travelers_info}}
        return self.client.post('/v1/booking/flight-orders', body)
