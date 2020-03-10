# Support Python 2 and 3 API calls without importing
# a 3rd party library

import json

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

        self.headers = {
            'User-Agent': self.__build_user_agent(),
            'Accept': 'application/json, application/vnd.amadeus+json',
            'Content-Type': 'application/vnd.amadeus+json'
        }

        self.url = self.__build_url()
        self.http_request = self.__build_http_request()

    # PRIVATE

    # Determines the User Agent
    def __build_user_agent(self):
        user_agent = 'amadeus-python/{0}'.format(self.client_version)
        user_agent += ' python/{0}'.format(self.language_version)
        if self.app_id:
            user_agent += ' {0}/{1}'.format(self.app_id, self.app_version)
        return user_agent

    # Builds a HTTP Request object based on the path, params, and verb
    def __build_http_request(self):
        # Requests token in case has not been set
        if (self.bearer_token is None):
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
            return HTTPRequest(self.url,
                               data=urlencode(self.params).encode(),
                               headers=self.headers)

        # Adds the authentication header since the bearer token has been set
        self.headers['Authorization'] = self.bearer_token

        if (self.verb == 'GET' or self.verb == 'DELETE'):
            return HTTPRequest(self.url, headers=self.headers)
        else:
            return HTTPRequest(self.url,
                               data=json.dumps(self.params).encode(),
                               headers=self.headers)

    # Encodes the params before sending them
    def _encoded_params(self):
        return self._urlencode(self.params)

    # Builds up the full URL based on the scheme, host, path, and params
    def __build_url(self):
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

    # Helper method to prepare the parameter encoding
    def _urlencode(self, d):
        return urlencode(self._flatten_keys(d, '', {}))

    # Flattens the hash keys, so page: { offset: 1 } becomes page[offet] = 1
    def _flatten_keys(self, d, key, out):
        if type(d) is not dict:
            raise TypeError('Only dicts can be encoded')

        for k in d:
            keystr = k if not key else '[{}]'.format(k)
            if type(d[k]) is dict:
                self._flatten_keys(d[k], str(key) + str(keystr), out)
            else:
                out['{}{}'.format(key, keystr)] = d[k]
        return out
