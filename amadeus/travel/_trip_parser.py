from amadeus.client.decorator import Decorator
from amadeus.travel.trip_parser._status import TripParserStatus
from amadeus.travel.trip_parser._result import TripParserResult


class TripParser(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)

    def status(self, job_id):
        return TripParserStatus(self.client, job_id)

    def result(self, job_id):
        return TripParserResult(self.client, job_id)

    def post(self, body):
        '''
        Forecast traveler choices in the context of search & shopping.

        .. code-block:: python

            amadeus.shopping.flight_offers.prediction.post(
                amadeus.shopping.flight_offers.get(origin='MAD',
                destination='NYC',
                departureDate='2019-08-01'
            ).body
        )

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v2/travel/trip-parser-jobs', body)
