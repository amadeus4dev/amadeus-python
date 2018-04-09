import json

from amadeus.client.errors import ParserError, ServerError
from amadeus.client.errors import AuthenticationError, NetworkError
from amadeus.client.errors import NotFoundError, ClientError


class Parser(object):

    # PROTECTED

    # Tries to detect for appropriate errors
    def _detect_error(self, client):
        error = self.error_for(self.status_code, self.parsed)
        if error is not None:
            self.__raise_error(error, client)

    def error_for(self, status_code, parsed):  # noqa: C901
        if status_code is None:
            return NetworkError
        if status_code >= 500:
            return ServerError
        if status_code == 401:
            return AuthenticationError
        if status_code == 404:
            return NotFoundError
        if status_code >= 400:
            return ClientError
        if not parsed:
            return ParserError

    # Parses the HTTP status code
    def _parse_status_code(self):
        http_response = self.http_response
        self.status_code = getattr(http_response, 'status', None)
        self.status_code = getattr(http_response, 'code', self.status_code)

    # Tries to parse the received data from raw string to parsed data and into
    # a data object
    def _parse_data(self, client):
        self.parsed = False
        self.data = None
        self.body = None
        self.result = None
        self.headers = {}

        self.__parse_body_and_headers(self.http_response, client)
        self.result = self.__parse_json(client)
        if (self.result is not None):
            self.data = self.result.get('data', None)

    # PRIVATE

    # Logs and raises the error
    def __raise_error(self, error_class, client):
        error = error_class(self)
        error._log(client)
        raise error

    # Extract the body and headers
    def __parse_body_and_headers(self, http_response, client):
        if hasattr(http_response, 'getheaders'):
            self.headers = dict(http_response.getheaders()) or self.headers
        if hasattr(http_response, 'info'):
            self.headers = http_response.info() or self.headers
        if hasattr(http_response, 'read'):
            self.body = http_response.read()
        if hasattr(self.body, 'decode'):
            self.body = self.body.decode('utf8')

    # Tries to parse the JSON, if there is any
    def __parse_json(self, client):
        try:
            if (self.__is_json()):
                result = json.loads(self.body)
                self.parsed = True
                return result
            else:
                return None
        except Exception:
            self.__raise_error(ParserError, client)

    # checks if the HTTPResponse included JSON
    def __is_json(self):
        return self.__has_json_header() and self.__has_body()

    # checks if the HTTPResponse has a non-empty body
    def __has_body(self):
        return self.body and len(self.body) > 0

    # checks if the HTTPResponse has a JSON header
    def __has_json_header(self):
        content_type = self.headers.get('Content-Type', None)
        if (content_type is not None):
            types = content_type.split(';')[0]
            types = ['application/json', 'application/vnd.amadeus+json']
            return content_type in types
        else:
            return False
