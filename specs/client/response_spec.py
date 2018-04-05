from mamba import description, context, it
from expects import expect, equal
from doublex import Stub
from amadeus_sdk import Response, Request

with description('Response') as self:
    with context('.__init__'):
        with it('should take a http response object and request'):
            http_response = Stub('http_response')
            request = Stub(Request)
            response = Response(http_response, request)
            expect(response.http_response).to(equal(http_response))
            expect(response.request).to(equal(request))
