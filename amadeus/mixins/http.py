from platform import python_version
from pprint import pformat
try:
    from urllib.error import URLError
except ImportError:  # pragma: no cover
    from urllib2 import Request as URLError  # pragma: no cover

from amadeus.version import version
from amadeus.client.request import Request
from amadeus.client.response import Response
from amadeus.client.access_token import AccessToken


# A helper module for making generic API calls. It is used by
# every namespaced API method.
class HTTP(object):
    '''
    A helper module for making generic API calls. It is used by
    every namespaced API method.
    '''

    def get(self, path, **params):
        '''
        A helper function for making generic GET requests calls. It is used by
        every namespaced API GET method.

        It can be used to make any generic API call that is automatically
        authenticated using your API credentials:

        .. code-block:: python

            amadeus.get('/foo/bar', airline='1X')

        :param path: path the full path for the API call
        :paramtype path: str

        :param params: (optional) params to pass to the API
        :paramtype params: dict

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: when the request fails
        '''
        return self.request('GET', path, params)

    def post(self, path, params={}):
        '''
        A helper function for making generic POST requests calls. It is used by
        every namespaced API POST method.

        It can be used to make any generic API call that is automatically
        authenticated using your API credentials:

        .. code-block:: python

            amadeus.post('/foo/bar', airline='1X')

        :param path: path the full path for the API call
        :paramtype path: str

        :param params: (optional) params to pass to the API
        :paramtype params: dict

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: when the request fails
        '''
        return self.request('POST', path, params)

    def delete(self, path, **params):
        '''
        A helper function for making generic DELETE requests calls. It is used by
        every namespaced API DELETE method.

        It can be used to make any generic API call that is automatically
        authenticated using your API credentials:

        .. code-block:: python

            amadeus.delete('/foo/bar', airline='1X')

        :param path: path the full path for the API call
        :paramtype path: str

        :param params: (optional) params to pass to the API
        :paramtype params: dict

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: when the request fails
        '''
        return self.request('DELETE', path, params)

    def request(self, verb, path, params):
        '''
        A helper function for making generic POST requests calls. It is used by
        every namespaced API method. It can be used to make any generic API
        call that is automatically authenticated using your API credentials:

        .. code-block:: python

          amadeus.request('GET', '/foo/bar', airline='1X')

        :param verb: the HTTP verb to use
        :paramtype verb: str

        :param path: path the full path for the API call
        :paramtype path: str

        :param params: (optional) params to pass to the API
        :paramtype params: dict

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: when the request fails
        '''
        return self._unauthenticated_request(
            verb, path, params,
            self.__access_token()._bearer_token()
        )

    # PROTECTED

    # Builds the URI, the request object, and makes the actual API calls.
    #
    # Used by the AccessToken to fetch a new Bearer Token
    #
    # Passes the response to a Response object for further parsing.
    #
    def _unauthenticated_request(self, verb, path, params, bearer_token=None):
        request = self.__build_request(verb, path, params, bearer_token)
        self.__log(request)
        return self.__execute(request)

    # PRIVATE

    # Builds a HTTP request object that contains all the information about
    # this request
    def __build_request(self, verb, path, params, bearer_token):
        return Request({
            'host': self.host,
            'verb': verb,
            'path': path,
            'params': params,
            'bearer_token': bearer_token,
            'client_version': version,
            'language_version': python_version(),
            'app_id': self.custom_app_id,
            'app_version': self.custom_app_version,
            'ssl': self.ssl,
            'port': self.port
        })

    # Executes the request and wraps it in a Response
    def __execute(self, request):
        http_response = self.__fetch(request)
        response = Response(http_response, request)._parse(self)
        self.__log(response)
        response._detect_error(self)
        return response

    # A memoized AccessToken object, so we don't keep reauthenticating
    def __access_token(self):
        if (not hasattr(self, 'access_token')):
            self.access_token = AccessToken(self)
        return self.access_token

    # Log any object
    def __log(self, object):
        if (self.log_level == 'debug'):
            self.logger.debug(
                '%s\n%s', object.__class__.__name__, pformat(object.__dict__)
            )

    # Actually make the HTTP call, making sure to catch it in case of an error
    def __fetch(self, request):
        try:
            return self.http(request.http_request)
        except URLError as exception:
            return exception
