from mamba import description, context, it, before
from expects import expect, equal
from doublex import Stub, Spy, ANY_ARG
from doublex_expects import have_been_called_with, have_been_called

from amadeus import Client, Request
from amadeus.client.access_token import AccessToken

with description('AccessToken') as self:
    with context('.bearer_token'):
        with before.each:
            request = Stub(Request)
            request.result = {
                'access_token': 'abc',
                'expires_in': 1799
            }
            with Spy(Client) as client:
                client._unauthenticated_request(ANY_ARG).returns(request)

            client.client_id = '123'
            client.client_secret = '234'
            self.client = client

        with it('should make a new API call if no token has been loaded yet'):
            access_token = AccessToken(self.client)
            expect(access_token._bearer_token()).to(equal('Bearer abc'))

            expect(self.client._unauthenticated_request).to(
                have_been_called_with(
                    'POST', '/v1/security/oauth2/token',
                    {
                        'grant_type': 'client_credentials',
                        'client_id': '123',
                        'client_secret': '234'
                    })
            )

        with it('should return a cached token if it still valid'):
            access_token = AccessToken(self.client)
            expect(access_token._bearer_token()).to(equal('Bearer abc'))
            expect(access_token._bearer_token()).to(equal('Bearer abc'))

            expect(self.client._unauthenticated_request).to(
                have_been_called.once
            )

        with it('should return a cached token if it still valid'):
            access_token = AccessToken(self.client)
            expect(access_token._bearer_token()).to(equal('Bearer abc'))
            access_token.expires_at = 0
            expect(access_token._bearer_token()).to(equal('Bearer abc'))

            expect(self.client._unauthenticated_request).to(
                have_been_called.twice
            )
