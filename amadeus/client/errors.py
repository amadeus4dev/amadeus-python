from pprint import pformat


class ResponseError(RuntimeError):
    """
    The response object containing the raw HTTP response and the request
    used to make the API call.
    """

    def __init__(self, response):
        self.response = response
        self.description = self.__determine_description()
        self.code = self.__determine_code()
        RuntimeError.__init__(self, self.description)

    # PROTECTED

    # Log the error
    def _log(self, client):
        if (client.log_level == 'warn'):
            client.logger.warning(
                'Amadeus %s: %s', self.code, pformat(self.description)
            )

    # PRIVATE

    # extracts the error description from the response, if it exists
    def __determine_description(self):
        if (self.response and self.response.parsed):
            result = self.response.result
            if 'errors' in result:
                return result['errors']
            if 'error_description' in result:
                return result

    # sets the error code to the name of this class
    def __determine_code(self):
        return self.__class__.__name__


class NetworkError(ResponseError):
    """
    This error occurs when there is some kind of error in the network
    """
    pass


class ParserError(ResponseError):
    """
    This error occurs when the response type was JSOn but could not be parsed
    """
    pass


class ServerError(ResponseError):
    """
    This error occurs when there is an error on the server
    """
    pass


class ClientError(ResponseError):
    """
    This error occurs when the client did not provide the right parameters
    """
    pass


class AuthenticationError(ResponseError):
    """
    This error occurs when the client did not provide the right credentials
    """
    pass


class NotFoundError(ResponseError):
    """
    This error occurs when the path could not be found
    """
    pass
