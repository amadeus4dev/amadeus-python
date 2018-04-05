from mamba import description, context, it, before
from doublex import Stub, Spy, ANY_ARG
from doublex_expects import have_been_called_with
from expects import expect, equal, be_none

from amadeus_sdk import Client, Response, Request
from amadeus_sdk.mixins.pagination import Pagination

with description('Pagination') as self:
    with before.all:
        # Initialize the client and pagination object
        self.next_response = Stub(Response)
        with Spy(Client) as client:
            client.request(ANY_ARG).returns(self.next_response)
        self.client = client
        self.pagination = Pagination()
        self.pagination.request = self.client.request

        # Initialize the previous request made and response received
        request = Stub(Request)
        request.verb = self.verb = 'GET'
        request.path = self.path = '/a'
        request.params = self.params = {'a': 'b'}
        self.response = Response(Stub('http_response'), request)

    with context('Client.previous'):
        with it('should create a new request with the page and call it'):
            self.response.result = {
                'meta': {'links': {'previous': 'http://f.co?page=1'}}
            }

            next_response = self.pagination.previous(self.response)
            expect(self.client.request).to(
                have_been_called_with('GET', '/a', a='b', page={'offset': '1'})
            )
            expect(next_response).to(equal(self.next_response))

        with it('should return nil if the page was not found'):
            self.response.result = {'meta': {'links': {}}}
            next_response = self.pagination.previous(self.response)
            expect(next_response).to(be_none)

    with context('Client.next'):
        with it('should create a new request with the page and call it'):
            self.response.result = {
                'meta': {'links': {'next': 'http://f.co?page=1'}}
            }

            next_response = self.pagination.next(self.response)
            expect(self.client.request).to(
                have_been_called_with('GET', '/a', a='b', page={'offset': '1'})
            )
            expect(next_response).to(equal(self.next_response))

        with it('should return nil if the page was not found'):
            self.response.result = {'meta': {'links': {}}}
            next_response = self.pagination.next(self.response)
            expect(next_response).to(be_none)

    with context('Client.first'):
        with it('should create a new request with the page and call it'):
            self.response.result = {
                'meta': {'links': {'first': 'http://f.co?page=1'}}
            }

            next_response = self.pagination.first(self.response)
            expect(self.client.request).to(
                have_been_called_with('GET', '/a', a='b', page={'offset': '1'})
            )
            expect(next_response).to(equal(self.next_response))

        with it('should return nil if the page was not found'):
            self.response.result = {'meta': {'links': {}}}
            next_response = self.pagination.first(self.response)
            expect(next_response).to(be_none)

    with context('Client.last'):
        with it('should create a new request with the page and call it'):
            self.response.request.params = {'page': {'offset': '0'}}
            self.response.result = {
                'meta': {'links': {'last': 'http://f.co?page=1'}}
            }

            next_response = self.pagination.last(self.response)
            expect(self.client.request).to(
                have_been_called_with('GET', '/a', a='b', page={'offset': '1'})
            )
            expect(next_response).to(equal(self.next_response))

        with it('should return nil if the page was not found'):
            self.response.result = {'meta': {'links': {}}}
            next_response = self.pagination.last(self.response)
            expect(next_response).to(be_none)
