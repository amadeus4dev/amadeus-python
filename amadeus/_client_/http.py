# Support Ruby 2 and 3 without importing a 3rd party library
try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, Request, HTTPError
    from urllib import urlencode

class HTTP(object):
    
    def get(self, url, data={}):
        return self._call('GET', url, data)

    def post(self, url, data={}):
        return self._call('POST', url, data)

    def _call(self, verb, url, data=None):
        if (data is not None) :
            data = urlencode(data).encode()
            if (verb == 'GET') :
                url = "{0}?{1}".format(url, data)
                data = None
            request = Request(url, data)
        else :
            request = Request(url)

        try:
            return self.http(request).read().decode()
        except HTTPError as error:
            print(request.get_method)
            return error.read().decode()
