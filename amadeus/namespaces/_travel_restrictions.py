from amadeus.client.decorator import Decorator
from amadeus.travel_restrictions import Covid19AreaReport


class TravelRestrictions(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.covid19_area_report = Covid19AreaReport(client)
