from mamba import description, context, it, before
from expects import expect, equal, raise_error, be_a, be
from doublex import Stub
from amadeus import Response, Request, Client
from amadeus import NetworkError, ServerError, AuthenticationError
from amadeus import NotFoundError, ClientError, ParserError


with description('Mixins/Parser') as self:
    with context('Response._parse'):
        with context('with a JSON content type'):
            with before.all:
                self.request = Stub(Request)
                with Stub(Client) as client:
                    client.log_level = 'silent'
                self.client = client

            with it('should parse the body'):
                with Stub() as http_response:
                    http_response.status_code = '200'
                    http_response.getheaders().returns(
                        [('Content-Type', 'application/json')]
                    )
                    http_response.read().returns('{ "data" : { "a" : 1 } }')

                response = Response(http_response, self.request)
                response = response._parse(self.client)
                expect(response.data).to(equal({'a': 1}))
                expect(response).to(be_a(Response))

            with it('should parse the body for content type vnd.amadeus+json'):
                with Stub() as http_response:
                    http_response.status_code = '200'
                    http_response.getheaders().returns(
                        [('Content-Type', 'application/vnd.amadeus+json')]
                    )
                    http_response.read().returns('{ "data" : { "a" : 1 } }')

                response = Response(http_response, self.request)
                response._parse(self.client)
                expect(response.data).to(equal({'a': 1}))

            with it('should not parse body if status code equal to 204'):
                with Stub() as http_response:
                    http_response.status_code = '204'
                    http_response.getheaders().returns(
                        [('Content-Type', 'application/vnd.amadeus+json')]
                    )

                response = Response(http_response, self.request)
                response._parse(self.client)
                expect(response.parsed).to(equal(False))
                expect(response.body).to(equal(None))
                expect(response.result).to(be(None))
                expect(response.data).to(be(None))

            with it('should parse no body for other content types'):
                with Stub() as http_response:
                    http_response.status_code = '200'
                    http_response.getheaders().returns(
                        [('Content-Type', 'plain/text')]
                    )
                    http_response.read().returns(u'Hello World')

                response = Response(http_response, self.request)
                response._parse(self.client)
                expect(response.body).to(equal('Hello World'))
                expect(response.result).to(be(None))
                expect(response.data).to(be(None))

            with it('should parse no body for a missing content type'):
                with Stub() as http_response:
                    http_response.status_code = '200'
                    http_response.getheaders().returns([])
                    http_response.read().returns('Hello World')

                response = Response(http_response, self.request)
                response._parse(self.client)
                expect(response.body).to(equal('Hello World'))
                expect(response.result).to(be(None))
                expect(response.data).to(be(None))

            with it('should raise a ParseError if it could not be parsed'):
                with Stub() as http_response:
                    http_response.status_code = '200'
                    http_response.getheaders().returns(
                        [('Content-Type', 'application/json')]
                    )
                    http_response.read().returns('{')

                response = Response(http_response, self.request)
                expect(lambda: response._parse(self.client)).to(
                    raise_error(ParserError)
                )

    with context('Response._detect_error'):
        with before.all:
            http_response = Stub()
            request = Stub(Request)
            self.client = Stub(Client)
            self.client.log_level = 'silent'
            self.response = Response(http_response, request)

        with it('should raise a network error if no status code was found'):
            self.response.status_code = None
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(NetworkError)
            )

        with it('should raise a server error if a 500 occured'):
            self.response.status_code = 500
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(ServerError)
            )

        with it('should raise a authentication error if a 401 happened'):
            self.response.status_code = 401
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(AuthenticationError)
            )

        with it('should raise a not found error if a 404 happened'):
            self.response.status_code = 404
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(NotFoundError)
            )

        with it('should raise a generic client error for any other 4XX error'):
            self.response.status_code = 400
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(ClientError)
            )

        with it('should raise a parser error if the result was not parsed'):
            self.response.status_code = 200
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).to(
                raise_error(ParserError)
            )

        with it('should not raise parse error for 204 responses'):
            self.response.status_code = 204
            self.response.parsed = False
            expect(lambda: self.response._detect_error(self.client)).not_to(
                raise_error(ParserError)
            )
