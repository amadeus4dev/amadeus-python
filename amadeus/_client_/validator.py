from os import environ
from logging import getLogger

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


class Validator(object):
    def init_required(self, key, options):
        value = self.init_optional(key, options)
        if (value is None):
            raise ValueError("Missing required argument: {0}".format(key))
        return value

    def init_optional(self, key, options, default=None):
        value = options.get(key, None)
        if (value is None):
            env_key = "AMADEUS_{0}".format(key.upper())
            value = environ.get(env_key, None)
        if (value is None):
            value = default
        return value

    def warn_on_unrecognized_options(self, options, logger, valid_options):
        for key in options:
            if (key in valid_options):
                continue
            logger.warning("Unrecognized option: {0}".format(key))

    def initialize_client_credentials(self, options):
        self.client_id = self.init_required('client_id', options)
        self.client_secret = self.init_required('client_secret', options)

    def initialize_logger(self, options):
        self.logger = self.init_optional('logger', options,
                                         getLogger('amadeus'))
        self.log_level = self.init_optional('log_level', options, 'warn')

    def initialize_host(self, options):
        self.hostname = self.init_optional('hostname', options, 'test')
        self.host = self.init_optional('host', options,
                                       self.HOSTS[self.hostname])
        self.ssl = self.init_optional('ssl', options, True)
        self.port = self.init_optional('port', options, 443)

    def initialize_custom_app(self, options):
        self.custom_app_id = self.init_optional('custom_app_id', options, None)
        self.custom_app_version = self.init_optional('custom_app_version',
                                                     options, None)

    def initialize_http(self, options):
        self.http = self.init_optional('http', options, urlopen)
