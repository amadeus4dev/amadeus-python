from amadeus.client.decorator import Decorator
from amadeus.travel.trip_parser_jobs._status import TripParserStatus
from amadeus.travel.trip_parser_jobs._result import TripParserResult


class TripParser(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)

    def status(self, job_id):
        return TripParserStatus(self.client, job_id)

    def result(self, job_id):
        return TripParserResult(self.client, job_id)

    def post(self, body):
        '''
        Sends the request for the parsing with the
        booking details and input parameters.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.post(
            '{ "data": {
             "type": "trip-parser-job",
             "content": : "base64string" }}'

        You can call our helper functions with your booking details
        in a file or the content encoded in Base64

        .. code-block:: python
            amadeus.travel.trip_parser_jobs.post(amadeus.travel.from_file(path_to_file))
            amadeus.travel.trip_parser_jobs.post(amadeus.travel.from_base64(base64))

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v2/travel/trip-parser-jobs', body)
