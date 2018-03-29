from amadeus.mixins.parser import Parser


class Response(Parser, object):
    '''
    The response object returned for every API call.

    :var http_response: the raw http response

    :var request: the original Request object used to make this call
    :vartype request: amadeus.Request

    :var result: the parsed JSON received from the API, if the result was JSON
    :vartype result: dict

    :var data: the data extracted from the JSON data, if the body contained
        JSON
    :vartype data: dict

    :var body: the raw body received from the API
    :vartype body: str

    :var parsed: wether the raw body has been parsed into JSON
    :vartype parsed: bool

    :var status_code: The HTTP status code for the response, if any
    :vartype status_code: int
    '''

    # Initialize the Response object with the
    # HTTPResponse object to parse, the client that made the request
    # and the original request made
    def __init__(self, http_response, request):
        self.http_response = http_response
        self.request = request

    # PROTECTED

    # Parses the response, using the client to log any errors
    def _parse(self, client):
        self._parse_status_code()
        self._parse_data(client)
        return self
