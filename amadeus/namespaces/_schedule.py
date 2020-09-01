from amadeus.client.decorator import Decorator
from amadeus.schedule._flights import Flights


class Schedule(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flights = Flights(client)
