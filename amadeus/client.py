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

    # The initialization method for the entire module
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

        Parameters
        ----------
        clientId : str
            the API key used to authenticate the API
        clientSecret : str
            the API secret used to authenticate the API
        logger : Logger (defaults to a new Logger)
            a Logger-compatible logger that accepts a "warning" call
        log_level : str (defaults to 'warn')
            if this client is running in debug, warn, or silent mode
        hostname : str (defaults to 'test')
            the name of the server API calls are made to, "production"
            or "test"
        custom_app_id : str (defaults to None)
            a custom App ID to be passed in the User Agent to the server
        custom_app_version : (defaults to None)
            a custom App Version number to be passed in the User Agent
            to the server
        http : urlopen (defaults to urlopen)
            an optional urlopen compatible client that accepts a Request object
        ssl : bool (defaults to True)
            if this client is will use HTTPS

        Returns
        -------
        Client
            An amadeus

        Raises
        ------
        ValueError
            If a require parameter is missing
        """

        self._initialize_client_credentials(options)
        self._initialize_logger(options)
        self._initialize_host(options)
        self._initialize_custom_app(options)
        self._initialize_http(options)

        recognized_options = ['client_id', 'client_secret', 'logger', 'host',
                              'hostname', 'custom_app_id',
                              'custom_app_version', 'http',
                              'log_level', 'ssl', 'port']
        self._warn_on_unrecognized_options(options, self.logger,
                                           recognized_options)
