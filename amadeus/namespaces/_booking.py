from amadeus.booking._flight_orders import FlightOrders
from amadeus.client.decorator import Decorator


class Booking(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_orders = FlightOrders(client)


__all__ = ['FlightOrders']
