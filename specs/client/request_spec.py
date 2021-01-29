from mamba import description, context, it, before
from expects import expect, equal, be_true, be_none, be_a
from amadeus import Request

from urllib.request import Request as HTTPRequest


with description('Request') as self:
    with before.all:
        self.host = 'example.com'
        self.verb = 'GET'
        self.path = '/foo/bar'
        self.params = {'foo': 'bar'}
        self.bearer_token = 'Bearer 123'
        self.client_version = '1.2.3'
        self.lang_version = '2.3.4'
        self.app_id = 'amadeus-cli'
        self.app_version = '3.4.5'
        self.ssl = True
        self.port = 443

        self.request = Request({
            'host': self.host,
            'verb': self.verb,
            'path': self.path,
            'params': self.params,
            'bearer_token': self.bearer_token,
            'client_version': self.client_version,
            'language_version': self.lang_version,
            'app_id': self.app_id,
            'app_version': self.app_version,
            'ssl': self.ssl,
            'port': self.port
        })

    with context('.__init__'):
        with it('should store the params'):
            expect(self.request.host).to(equal(self.host))
            expect(self.request.port).to(equal(self.port))
            expect(self.request.ssl).to(be_true)
            expect(self.request.scheme).to(equal('https'))
            expect(self.request.verb).to(equal(self.verb))
            expect(self.request.path).to(equal(self.path))
            expect(self.request.params).to(equal(self.params))
            expect(self.request.bearer_token).to(equal(self.bearer_token))
            expect(self.request.client_version).to(equal(self.client_version))
            expect(self.request.language_version).to(equal(self.lang_version))
            expect(self.request.app_id).to(equal(self.app_id))
            expect(self.request.app_version).to(equal(self.app_version))

    with context('.http_request'):
        with it('should return a GET HTTP Request'):
            expect(self.request.http_request).to(be_a(HTTPRequest))
            expect(self.request.http_request.data).to(be_none)
            expect(
                self.request.http_request.get_header('Content-Type', None)
            ).to(be_none)
            expect(self.request.http_request.get_header('Authorization')).to(
                equal(self.bearer_token)
            )
            expect(self.request.http_request.get_header('Accept')).to(
                equal('application/json, application/vnd.amadeus+json')
            )
            expect(self.request.http_request.get_header('User-agent')).to(
                equal('amadeus-python/1.2.3 python/2.3.4 amadeus-cli/3.4.5')
            )

        with it('should return a POST HTTP Request'):
            self.request = Request({
                'host': self.host,
                'verb': 'POST',
                'path': self.path,
                'params': self.params,
                'bearer_token': self.bearer_token,
                'client_version': self.client_version,
                'language_version': self.lang_version,
                'app_id': self.app_id,
                'app_version': self.app_version,
                'port': self.port,
                'ssl': self.ssl
            })

            expect(self.request.http_request).to(be_a(HTTPRequest))
            expect(self.request.http_request.get_full_url()).to(equal(
                'https://example.com/foo/bar'))
            expect(self.request.http_request.data).to(
                equal(b'{\"foo\": \"bar\"}'))

        with it('should handle a custom scheme and port'):
            self.request = Request({
                'host': self.host,
                'verb': 'POST',
                'path': self.path,
                'params': self.params,
                'bearer_token': self.bearer_token,
                'client_version': self.client_version,
                'language_version': self.lang_version,
                'app_id': self.app_id,
                'app_version': self.app_version,
                'port': 8080,
                'ssl': False
            })

            expect(self.request.http_request.get_full_url()).to(equal(
                'http://example.com:8080/foo/bar'))
