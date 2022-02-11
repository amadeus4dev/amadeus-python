from amadeus.client.decorator import Decorator
from amadeus.duty_of_care._diseases import Diseases


class DutyOfCare(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.diseases = Diseases(client)
