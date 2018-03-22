from ._client_.validator import Validator
from ._client_.http import HTTP


class Client(Validator, HTTP, object):
    """
    The Amadeus client library for accessing
    the travel APIs.
    """

    # The available hosts for this API
    HOSTS = {
      'test': 'test.api.amadeus.com',
      'production': 'production.api.amadeus.com'
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
                              'hostname', 'custom_app_id',
                              'custom_app_version', 'http',
                              'log_level', 'ssl', 'port']
        self.warn_on_unrecognized_options(options, self.logger,
                                          recognized_options)
