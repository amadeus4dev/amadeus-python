from pprint import pformat


class ResponseError(RuntimeError):
    '''
    An Amadeus error

    :var response: The response object containing the raw HTTP response and
        the request used to make the API call.
    :vartype response: amadeus.Response

    :var code: A unique code for this type of error. Options include
        ``NetworkError``, ``ParserError``, ``ServerError``,
        ``AuthenticationError``, ``NotFoundError`` and ``UnknownError``.
    :vartype code: str
    '''

    def __init__(self, response):
        self.response = response
        self.code = self.__determine_code()
        RuntimeError.__init__(self, self.description())

    # PROTECTED

    # Log the error
    def _log(self, client):
        if (client.log_level == 'warn'):
            client.logger.warning(
                'Amadeus %s: %s', self.code, pformat(self.description)
            )

    # PRIVATE

    # Determines the description for this error, as used in in the error output
    def description(self):
        description = self.short_description(self.response)
        return description + self.long_description(self.response)

    # Determines the short description, printed after on the same line as the
    # error class name
    def short_description(self, response):
        if hasattr(response, 'status_code') and response.status_code:
            return '[{0}]'.format(response.status_code)
        else:
            return '[---]'

    # Determines the longer description, printed after the initial error
    def long_description(self, response):
        message = ''
        if not(response and response.parsed):
            return message
        if 'error_description' in response.result:
            message += self.error_description(self.response)
        if 'errors' in response.result:
            message += self.errors_descriptions(self.response)
        return message

    # Returns the description of a single error
    def error_description(self, response):
        message = ''
        if 'error' in response.result:
            message += '\n{0}'.format(response.result['error'])
        message += '\n{0}'.format(response.result['error_description'])
        return message

    # Returns the description of multiple errors
    def errors_descriptions(self, response):
        messages = map(self.errors_description, response.result['errors'])
        return ''.join(messages)

    # Returns the description of a single error in a multi error response
    def errors_description(self, error):
        message = '\n'
        if ('source' in error) and ('parameter' in error['source']):
            message += '[{0}] '.format(error['source']['parameter'])
            if 'detail' in error:
                message += error['detail']
        return message

    # sets the error code to the name of this class
    def __determine_code(self):
        return self.__class__.__name__


class NetworkError(ResponseError):
    '''
    This error occurs when there is some kind of error in the network
    '''
    pass


class ParserError(ResponseError):
    '''
    This error occurs when the response type was JSOn but could not be parsed
    '''
    pass


class ServerError(ResponseError):
    '''
    This error occurs when there is an error on the server
    '''
    pass


class ClientError(ResponseError):
    '''
    This error occurs when the client did not provide the right parameters
    '''
    pass


class AuthenticationError(ResponseError):
    '''
    This error occurs when the client did not provide the right credentials
    '''
    pass


class NotFoundError(ResponseError):
    '''
    This error occurs when the path could not be found
    '''
    pass
