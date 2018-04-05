# Support Python 2 and 3 API calls without importing
# a 3rd party library
try:
    from urllib.request import Request as HTTPRequest
    from urllib.parse import urlencode
except ImportError:  # pragma: no cover
    from urllib2 import Request as HTTPRequest  # pragma: no cover
    from urllib import urlencode  # pragma: no cover


class Request(object):
    '''
    An object containing all the compiled information about the request made.

    :var host: The host used for this API call
    :vartype host: str

    :var port: The port for this API call. Standard set to 443.
    :vartype port: int

    :var ssl: Wether to use SSL for a call, defaults to true
    :vartype ssl: bool

    :var scheme: The scheme used to make the API call
    :vartype scheme: str

    :var params: The GET/POST params for the API call
    :vartype params: dict

    :var path: The path of the API to be called
    :vartype path: str

    :var verb: The verb used to make an API call ('GET' or 'POST')
    :vartype verb: str

    :var bearer_token: The bearer token (if any) that was used for
        authentication
    :vartype bearer_token: str

    :var headers: The headers used for the API call
    :vartype headers: dict

    :var client_version: The library version used for this request
    :vartype client_version: str

    :var language_version: The Python language version used for this request
    :vartype language_version: str

    :var app_id: The custom app ID passed in for this request
    :vartype app_id: str

    :var app_version: The custom app version used for this request
    :vartype app_version: str
    '''

    def __init__(self, options):
        self.http_request = None
        self.__initialize_options(options)
        self.__initialize_headers()
        self.__build_http_request()

    # PRIVATE

    # Initializes the Request object with all the passed in params. These
    # do not change once set
    def __initialize_options(self, options):
        self.host = options['host']
        self.port = options['port']
        self.ssl = options['ssl']
        self.scheme = 'https' if self.ssl else 'http'
        self.verb = options['verb']
        self.path = options['path']
        self.params = options['params']
        self.bearer_token = options['bearer_token']
        self.client_version = options['client_version']
        self.language_version = options['language_version']
        self.app_id = options['app_id']
        self.app_version = options['app_version']

    # Initializes the basic headers
    def __initialize_headers(self):
        self.headers = {
            'User-Agent': self.__build_user_agent(),
            'Accept': 'application/json, application/vnd.amadeus+json'
        }

    # Determines the User Agent
    def __build_user_agent(self):
        user_agent = 'amadeus-python/{0}'.format(self.client_version)
        user_agent += ' python/{0}'.format(self.language_version)
        if self.app_id:
            user_agent += ' {0}/{1}'.format(self.app_id, self.app_version)
        return user_agent

    # Builds up a HTTP Request objectm if not akready set
    def __build_http_request(self):
        request = self.__request_for_verb()
        self.__add_post_data_header()
        self.__add_bearer_token_header()
        self.__apply_headers(request)
        self.http_request = request

    # Builds a HTTP Request object based on the path, params, and verb
    def __request_for_verb(self):
        params = self._encoded_params().encode()
        path = self.__full_url()

        if (self.verb == 'GET'):
            return HTTPRequest(path)
        else:
            return HTTPRequest(path, params)

    # Encodes the params before sending them
    def _encoded_params(self):
        return urlencode(self.params)

    # Builds up the full URL based on the scheme, host, path, and params
    def __full_url(self):
        full_url = '{0}://{1}'.format(self.scheme, self.host)
        if not self.__port_matches_scheme():
            full_url = '{0}:{1}'.format(full_url, self.port)
        full_url = '{0}{1}'.format(full_url, self.path)
        if (self.verb == 'GET'):
            full_url += '?{0}'.format(self._encoded_params())
        return full_url

    def __port_matches_scheme(self):
        return ((self.ssl and self.port == 443) or
                (not self.ssl and self.port == 80))

    # Adds an extra header if the verb is POST
    def __add_post_data_header(self):
        if (self.verb == 'POST'):
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    # Adds the authentication header if the bearer token has been set
    def __add_bearer_token_header(self):
        if (self.bearer_token is not None):
            self.headers['Authorization'] = self.bearer_token

    # Applies all the headers to the HTTP Request object
    def __apply_headers(self, http_request):
        http_request.headers = self.headers
