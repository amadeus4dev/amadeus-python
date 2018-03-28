from mamba import description, context, it, before
from doublex import Spy, Stub, method_returning, method_raising
from doublex_expects import have_been_called_with, have_been_called
from expects import expect, equal, raise_error

try:
    from urllib.error import URLError
except ImportError:  # pragma: no cover
    from urllib2 import Request as URLError  # pragma: no cover

from amadeus import Client, Response, ResponseError

with description('HTTP') as self:
    with before.each:
        self.client = Client(
            client_id='123',
            client_secret='234',
            log_level='silent'
        )
        self.response = Stub(Response)
        self.request_method = method_returning(self.response)

    with context('Client.get'):
        with it('should pass all details to the request method'):
            self.client.request = self.request_method
            response = self.client.get('/foo', foo='bar')
            expect(response).to(equal(self.response))
            expect(self.client.request).to(
                have_been_called_with('GET', '/foo',  foo='bar')
            )

    with context('Client.post'):
        with it('should pass all details to the request method'):
            self.client.request = self.request_method
            response = self.client.post('/foo', foo='bar')
            expect(response).to(equal(self.response))
            expect(self.client.request).to(
                have_been_called_with('POST', '/foo',  foo='bar')
            )

    with context('Client.request'):
        with it('should pass on to the _unauthenticated_request method'):
            self.response.result = {'access_token': '123'}
            self.client._unauthenticated_request = self.request_method
            response = self.client.request('POST', '/foo', foo='bar')
            expect(response).to(equal(self.response))
            expect(self.client._unauthenticated_request).to(
                have_been_called_with(
                    'POST', '/foo', {'foo': 'bar'}, 'Bearer 123'
                )
            )

    with context('Client._unauthenticated_request'):
        with it('should execute a full request'):
            with Stub() as http_response:
                http_response.code = 200
                http_response.getheaders().returns(
                    [('Content-Type', 'application/json')]
                )
                http_response.read().returns('{ "data" : { "a" : 1 } }')

            self.client.http = method_returning(http_response)
            response = self.client._unauthenticated_request(
                'GET', '/foo', {}, None
            )
            expect(self.client.http).to(have_been_called.once)
            expect(self.response).to(equal(self.response))

        with it('should catch a HTTPError'):
            self.client.http = method_raising(URLError('Error'))
            expect(
                lambda: self.client._unauthenticated_request(
                    'GET', '/foo', {}, None
                )
            ).to(raise_error(ResponseError))

        with it('should log when in debug mode'):
            with Stub() as http_response:
                http_response.code = 200
                http_response.getheaders().returns(
                    [('Content-Type', 'application/json')]
                )
                http_response.read().returns('{ "data" : { "a" : 1 } }')

            self.client.http = method_returning(http_response)
            self.client.logger = Spy()
            self.client.log_level = 'debug'
            response = self.client._unauthenticated_request(
                'GET', '/foo', {}, None
            )
            expect(self.client.logger.debug).to(have_been_called.twice)
