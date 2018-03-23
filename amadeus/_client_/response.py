from amadeus._client_.response_parser import ResponseParser


class Response(ResponseParser, object):
    # Initialize the Response object with the
    # HTTPResponse object to parse, the client that made the request
    # and the original request made
    def __init__(self, http_response, request):
        self.http_response = http_response
        self.request = request

    # Parses the response, using the client to log any errors
    def parse(self, client):
        self._parse_status_code()
        self._parse_data(client)
        return self
