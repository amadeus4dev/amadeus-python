import logging

from ._client_.validator import Validator
from ._client_.http import HTTP, urlopen

class Client(Validator, HTTP, object):
    """
    The Amadeus client library for accessing
    the travel APIs
    """

    # The available hosts for this API
    HOSTS = {
      'test' : 'test.api.amadeus.com',
      'production' : 'production.api.amadeus.com'
    }

    def __init__(self, **options):
        """
        Initialize using your credentials:

          amadeus = amadeus.Client(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET'
          )

        Alternatively, initialize the library using
        the environment variables +AMADEUS_CLIENT_ID+
        and +AMADEUS_CLIENT_SECRET+

          amadeus = amadeus.Client()

        """

        self.initialize_client_credentials(options)
        self.initialize_logger(options)
        self.initialize_host(options)
        self.initialize_custom_app(options)
        self.initialize_http(options)

        recognized_options = ['client_id', 'client_secret', 'logger', 'host',
            'hostname', 'custom_app_id', 'custom_app_version', 'http',
            'log_level', 'ssl', 'port']
        self.warn_on_unrecognized_options(options, self.logger, recognized_options)


    def initialize_client_credentials(self, options):
        self.client_id     = self.init_required('client_id', options)
        self.client_secret = self.init_required('client_secret', options)

    def initialize_logger(self, options):
        self.logger       = self.init_optional('logger', options, logging.getLogger('amadeus'))
        self.log_level    = self.init_optional('log_level', options, 'warn')

    def initialize_host(self, options):
        self.hostname = self.init_optional('hostname', options, 'test')
        self.host = self.init_optional('host', options, self.HOSTS[self.hostname])
        self.ssl =  self.init_optional('ssl', options, True)
        self.port = self.init_optional('port', options, 443)

    def initialize_custom_app(self, options):
        self.custom_app_id = self.init_optional('custom_app_id', options, None)
        self.custom_app_version = self.init_optional('custom_app_version', options, None)

    def initialize_http(self, options):
        self.http = self.init_optional('http', options, urlopen)
