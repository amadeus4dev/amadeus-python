from pprint import pformat


class ResponseError(RuntimeError):
    def __init__(self, response):
        self.response = response
        self.description = self._determine_description()
        self.code = self._determine_code()
        RuntimeError.__init__(self, self.description)

    # PROTECTED

    # Log any object
    def log(self, client):
        if (client.log_level == 'warn'):
            client.logger.warning(
                'Amadeus %s: %s', self.code, pformat(self.description)
            )

    # PRIVATE

    # extracts the error description from the response, if it exists
    def _determine_description(self):
        if (self.response and self.response.parsed):
            result = self.response.result
            if 'errors' in result:
                return result['errors']
            if 'error_description' in result:
                return result['error_description']

    # sets the error code to the name of this class
    def _determine_code(self):
        return self.__class__.__name__


# This error occurs when there is some kind of error in the network
class NetworkError(ResponseError):
    pass


# This error occurs when the response type was JSOn but could not be parsed
class ParserError(ResponseError):
    pass


# This error occurs when there is an error on the server
class ServerError(ResponseError):
    pass


# This error occurs when the client did not provide the right parameters
class ClientError(ResponseError):
    pass


# This error occurs when the client did not provide the right credentials
class AuthenticationError(ResponseError):
    pass


# This error occurs when the path could not be found
class NotFoundError(ResponseError):
    pass
