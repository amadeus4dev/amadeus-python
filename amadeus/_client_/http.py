from platform import python_version
from pprint import pformat
try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import Request as HTTPError

from amadeus.version import version
from amadeus._client_.request import Request
from amadeus._client_.response import Response
from amadeus._client_.access_token import AccessToken


# A helper module for making generic API calls. It is used by
# every namespaced API method.
class HTTP(object):

    def get(self, path, **params):
        """
        A helper module for making generic GET requests calls. It is used by
        every namespaced API GET method.

          amadeus.reference_data.urls.checkin_links.get(airline='1X')

        It can be used to make any generic API call that is automatically
        authenticated using your API credentials:

          amadeus.get('/v2/reference-data/urls/checkin-links', airline='1X')

        """
        return self._request('GET', path, **params)

    def post(self, path, **params):
        """
        A helper module for making generic POST requests calls. It is used by
        every namespaced API POST method.

          amadeus.foo.bar.post(some='data')

        It can be used to make any generic API call that is automatically
        authenticated using your API credentials:

          amadeus.post('/v2/foo/bar', some='data')

        """
        return self._request('POST', path, **params)

    # PROTECTED

    # A more generic helper for making authenticated API calls
    def _request(self, verb, path, **params):
        return self._unauthenticated_request(
            verb, path, params,
            self._access_token().bearer_token()
        )

    # Builds the URI, the request object, and makes the actual API calls.
    #
    # Used by the AccessToken to fetch a new Bearer Token
    #
    # Passes the response to a Response object for further parsing.
    #
    def _unauthenticated_request(self, verb, path, params, bearer_token=None):
        request = self._build_request(verb, path, params, bearer_token)
        self._log(request)
        return self._execute(request)

    # PRIVATE

    # Builds a HTTP request object that contains all the information about
    # this request
    def _build_request(self, verb, path, params, bearer_token):
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
    def _execute(self, request):
        http_response = self._fetch(request)
        response = Response(http_response, request).parse(self)
        self._log(response)
        response.detect_error(self)
        return response

    # A memoized AccessToken object, so we don't keep reauthenticating
    def _access_token(self):
        if (not hasattr(self, 'access_token')):
            self.access_token = AccessToken(self)
        return self.access_token

    # Log any object
    def _log(self, object):
        if (self.log_level == 'debug'):
            self.logger.debug(
                '%s\n%s', object.__class__.__name__, pformat(object.__dict__)
            )

    # Actually make the HTTP call, making sure to catch it in case of an error
    def _fetch(self, request):
        try:
            return self.http(request.http_request)
        except HTTPError as exception:
            return exception
