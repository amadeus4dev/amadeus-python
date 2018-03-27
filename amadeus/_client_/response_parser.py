import json

from amadeus.errors import ParserError, ServerError, AuthenticationError
from amadeus.errors import NotFoundError, ClientError, NetworkError


class ResponseParser(object):
    # Tries to detect for appropriate errors
    def detect_error(self, client):
        if self.status_code is None:
            self._raise_error(NetworkError, client)
        if self.status_code >= 500:
            self._raise_error(ServerError, client)
        if self.status_code == 401:
            self._raise_error(AuthenticationError, client)
        if self.status_code == 404:
            self._raise_error(NotFoundError, client)
        if self.status_code >= 400:
            self._raise_error(ClientError, client)
        if not self.parsed:
            self._raise_error(ParserError, client)

    # PRIVATE

    # Parses the HTTP status code
    def _parse_status_code(self):
        self.status_code = None
        if hasattr(self.http_response, 'status'):
            self.status_code = self.http_response.status
        if hasattr(self.http_response, 'code'):
            self.status_code = self.http_response.code

    # Tries to parse the received data from raw string to parsed data and into
    # a data object
    def _parse_data(self, client):
        self.parsed = False
        self.data = None
        self.body = None
        self.result = None
        self.headers = {}

        self._parse_body_and_headers(self.http_response, client)
        self.result = self._parse_json(client)
        if (self.result is not None):
            self.data = self.result.get('data', None)

    # Logs and raises the error
    def _raise_error(self, error_class, client):
        error = error_class(self)
        error.log(client)
        raise error

    # Extract the body and headers
    def _parse_body_and_headers(self, http_response, client):
        if hasattr(http_response, 'getheaders'):
            self.headers = dict(http_response.getheaders())
        if hasattr(http_response, 'info'):
            self.headers = http_response.info()
        if hasattr(http_response, 'read'):
            self.body = http_response.read()

    # Tries to parse the JSON, if there is any
    def _parse_json(self, client):
        try:
            if (self._is_json()):
                result = json.loads(self.body)
                self.parsed = True
                return result
            else:
                return None
        except json.decoder.JSONDecodeError:
            self._raise_error(ParserError, client)

    # checks if the HTTPResponse included JSON
    def _is_json(self):
        return self._has_json_header() and self._has_body()

    # checks if the HTTPResponse has a non-empty body
    def _has_body(self):
        return self.body and len(self.body) > 0

    # checks if the HTTPResponse has a JSON header
    def _has_json_header(self):
        content_type = self.headers.get('Content-Type', None)
        if (content_type is not None):
            types = content_type.split(';')[0]
            types = ['application/json', 'application/vnd.amadeus+json']
            return content_type in types
        else:
            return False
