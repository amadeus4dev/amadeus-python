from amadeus.client.decorator import Decorator


class FlightOrders(Decorator, object):
    def post(self, flight, travelers, **params):
        '''
        Gets a confirmed price and availability of a flight

        .. code-block:: python

            amadeus.shopping.flight_offers.pricing.post(body, params)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        flight_offers = []
        if type(flight) is not list:
            flight_offers.append(flight)
        else:
            flight_offers.extend(flight)
        travelers_info = []
        if type(travelers) is not list:
            travelers_info.append(travelers)
        else:
            travelers_info.extend(travelers)

        return self.client.post('/v1/booking/flight-orders',
                                {'data':
                                    {'type': 'flight-order',
                                        'flightOffers': flight_offers},
                                    'travelers': travelers})
