import os
import sys
import logging

try:
    from urllib.request import urlopen
except ImportError:  # pragma: no cover
    from urllib2 import urlopen  # pragma: no cover


# A set of helper methods to allow the validating of
# arguments past into the Client
class Validator(object):

    # PROTECTED

    # Checks a list of options for unrecognized keys and warns the user.
    # This is mainly used to provide a nice experience when users make a typo
    # in their arguments.
    def _warn_on_unrecognized_options(self, options, logger, valid_options):
        for key in options:
            if (key in valid_options):
                continue
            logger.warning('Unrecognized option: {0}'.format(key))

    # Initializes the credentials, requiring an ID and Secret
    def _initialize_client_credentials(self, options):
        self.client_id = self.__init_required('client_id', options)
        self.client_secret = self.__init_required('client_secret', options)

    # Initializes an optional Logger
    def _initialize_logger(self, options):
        default_logger = logging.getLogger('amadeus')
        default_logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        default_logger.addHandler(handler)

        self.logger = self.__init_optional('logger', options, default_logger)
        self.log_level = self.__init_optional('log_level', options, 'silent')

    # Initializes an optional host, hostname, port, and SSL requirements
    def _initialize_host(self, options):
        self.hostname = self.__init_optional('hostname', options, 'test')
        self.host = self.__init_optional('host', options,
                                         self.HOSTS[self.hostname])
        self.ssl = self.__init_optional('ssl', options, True)
        self.port = self.__init_optional('port', options, 443)

    # Initializes an optional custom App ID and Version
    def _initialize_custom_app(self, options):
        self.custom_app_id = self.__init_optional('custom_app_id',
                                                  options, None)
        self.custom_app_version = self.__init_optional('custom_app_version',
                                                       options, None)

    # Initializes a custom http handler
    def _initialize_http(self, options):
        self.http = self.__init_optional('http', options, urlopen)

    # PRIVATE

    # Uses 'init_optional' to find an entry, and it that returns
    # nil it raises an ArgumentError
    #
    def __init_required(self, key, options):
        value = self.__init_optional(key, options)
        if (value is None):
            raise ValueError('Missing required argument: {0}'.format(key))
        return value

    # Tries to find an option by string or symbol in the options hash and
    # in the environment variables.When it can not find it anywhere it
    # defaults to the provided default option.
    def __init_optional(self, key, options, defa_ult=None):
        value = options.get(key, None)
        if (value is None):
            env_key = 'AMADEUS_{0}'.format(key.upper())
            value = os.environ.get(env_key, None)
        if (value is None):
            value = defa_ult
        return value
