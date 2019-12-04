import base64
import json
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

    def encode_email(self, email):
        '''
        Sends the .eml booking confirmation and
        returns the body to be sent in the POST request.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.encode_email(file)
        '''
        with open(email, 'rb') as email_file:
            encoded_email = base64.b64encode(email_file.read()).decode()
        return json.loads(
            '{"data": {"type": "trip-parser-job", "content": "'
            + encoded_email + '"}}')

    def encode_pdf(self, pdf):
        '''
        Sends the .pdf booking confirmation and
        returns the body to be sent in the POST request.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.encode_pdf(file)
        '''
        with open(pdf, 'rb') as pdf_file:
            encoded_pdf = base64.b64encode(pdf_file.read()).decode()
        return json.loads(
            '{"data": {"type": "trip-parser-job", "content": "'
            + encoded_pdf + '"}}')

    def encode_html(self, webpage):
        '''
        Sends the .html booking confirmation and
        returns the body to be sent in the POST request.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.encode_html(file)
        '''
        with open(webpage, 'rb') as html_webpage:
            encoded_webpage = base64.b64encode(html_webpage.read()).decode()
        return json.loads(
            '{"data": {"type": "trip-parser-job", "content": "'
            + encoded_webpage + '"}}')

    def post(self, body):
        '''
        Sends the request for the parsing with the
        booking details and input parameters.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.post(body)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post('/v2/travel/trip-parser-jobs', body)
