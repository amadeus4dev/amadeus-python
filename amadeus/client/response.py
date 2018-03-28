from amadeus.mixins.parser import Parser


class Response(Parser, object):
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
