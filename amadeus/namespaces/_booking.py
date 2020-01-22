from amadeus.booking._flight_orders import FlightOrders
from amadeus.booking._flight_order import FlightOrder
from amadeus.booking._hotel_bookings import HotelBookings
from amadeus.client.decorator import Decorator


class Booking(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_orders = FlightOrders(client)
        self.hotel_bookings = HotelBookings(client)

    def flight_order(self, flight_order_id):
        return FlightOrder(self.client, flight_order_id)


__all__ = ['FlightOrders', 'FlightOrder', 'HotelBookings']
