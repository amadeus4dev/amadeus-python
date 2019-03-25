from .mixins.validator import Validator
from .mixins.http import HTTP
from .mixins.pagination import Pagination
from .namespaces import Core as Namespaces


class Client(Namespaces, Pagination, Validator, HTTP, object):
    '''
    The Amadeus client library for accessing
    the travel APIs.
    '''

    # The available hosts for this API
    HOSTS = {
        'test': 'test.api.amadeus.com',
        'production': 'api.amadeus.com'
    }

    # The initialization method for the entire module
    def __init__(self, **options):
        '''
        Initialize using your credentials:

        .. code-block:: python


            from amadeus import Client

            amadeus = Client(
                client_id='YOUR_CLIENT_ID',
                client_secret='YOUR_CLIENT_SECRET'
            )

        Alternatively, initialize the library using the environment variables
        ``AMADEUS_CLIENT_ID`` and ``AMADEUS_CLIENT_SECRET``.

        .. code-block:: python


        amadeus = amadeus.Client()

        :param client_id: the API key used to authenticate the API
        :paramtype client_id: str

        :param client_secret: the API secret used to authenticate the API
        :paramtype client_secret: str

        :param logger: (optional) a Python compatible logger
            (Default: ``logging.Logger``)
        :paramtype logger: logging.Logger

        :param log_level: (optional) the log level of the client, either
            ``"debug"``, ``"warn"``, or ``"silent"`` mode
            (Default: ``"silent"``)
        :paramtype log_level: str

        :param hostname: (optional) the name of the server API calls are made
            to, ``"production"``  or ``"test"``. (Default: ``"test"``)
        :paramtype hostname: str

        :param host: (optional) alternatively, you can specify a full host
            domain name instead, e.g. ``"api.example.com"``
        :paramtype host: str

        :param ssl: if this client is should use HTTPS (Default: ``True``)
        :paramtype ssl: bool

        :param port: the port this client should use (Default: ``80`` for HTTP
            and ``443`` for HTTPS)
        :paramtype port: int

        :param custom_app_id: (optional) a custom App ID to be passed in
            the User Agent to the server (Default: ``None``)
        :paramtype custom_app_id: str

        :param custom_app_version: (optional) a custom App Version number to
            be passed in the User Agent to the server (Default: ``None``)
        :paramtype custom_app_version: str

        :param http: (optional) a :func:`urllib.request.urlopen` compatible
            client that accepts a :class:`urllib.request.Request` compatible
            object (Default: ``urlopen``)
        :paramtype http: urllib.request.urlopen

        :raises ValueError: when a required param is missing
        '''
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
        Namespaces.__init__(self)
