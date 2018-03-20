from os import environ

class Validator(object):

    def init_required(self, key, options):
        value = self.init_optional(key, options)
        if (value is None):
            raise ValueError("Missing required argument: {0}".format(key))
        return value

    def init_optional(self, key, options, default = None):
        value = options.get(key, None)
        if (value is None):
            env_key = "AMADEUS_{0}".format(key.upper())
            value = environ.get(env_key, None)
        if (value is None):
            value = default
        return value

    def warn_on_unrecognized_options(self, options, logger, recognized_options):
        for key in options:
            if (key in recognized_options) : continue
            logger.warning( "Unrecognized option: {0}".format(key)) 
