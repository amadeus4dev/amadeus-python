import pytest
import mock
from amadeus import Client, Response, Request
from amadeus.mixins.pagination import Pagination


@pytest.fixture
def self():
    # Initialize the client and pagination object
    self.next_response = mock.MagicMock(Response)
    client = mock.MagicMock(Client)
    client.request = self.next_response
    self.client = client
    self.pagination = Pagination()
    self.pagination.request = self.client.request

    # Initialize the previous request made and response received
    self.request = mock.MagicMock(Request)
    self.request.verb = self.verb = 'GET'
    self.request.path = self.path = '/a'
    self.request.params = self.params = {'a': 'b'}
    self.response = Response(mock.MagicMock('http_response'), self.request)
    return self


def test_create_new_request_when_previous(self):
    self.response.result = {
        'meta': {'links': {'previous': 'https://f.co?page%5Boffset%5D=1'}}
    }
    self.pagination.previous(self.response)
    self.client.request.call_args.assert_called_with(
        'GET', '/a', {'a': 'b', 'page': {'offset': '1'}})


def test_should_return_nil_page_not_found_with_previous(self):
    self.response.result = {'meta': {'links': {}}}
    next_response = self.pagination.previous(self.response)
    assert next_response is None


def test_create_new_request_when_next(self):
    self.response.result = {
        'meta': {'links': {'next': 'https://f.co?page%5Boffset%5D=1'}}
    }
    self.pagination.next(self.response)
    self.client.request.call_args.assert_called_with(
        'GET', '/a', {'a': 'b', 'page': {'offset': '1'}})


def test_should_return_nil_page_not_found_with_next(self):
    self.response.result = {'meta': {'links': {}}}
    next_response = self.pagination.next(self.response)
    assert next_response is None


def test_create_new_request_when_first(self):
    self.response.result = {
        'meta': {'links': {'first': 'https://f.co?page%5Boffset%5D=1'}}
    }
    self.pagination.first(self.response)
    self.client.request.call_args.assert_called_with(
        'GET', '/a', {'a': 'b', 'page': {'offset': '1'}})


def test_should_return_nil_page_not_found_with_first(self):
    self.response.result = {'meta': {'links': {}}}
    next_response = self.pagination.first(self.response)
    assert next_response is None


def test_create_new_request_when_last(self):
    self.response.result = {
        'meta': {'links': {'last': 'https://f.co?page%5Boffset%5D=1'}}
    }
    self.pagination.last(self.response)
    self.client.request.call_args.assert_called_with(
        'GET', '/a', {'a': 'b', 'page': {'offset': '1'}})


def test_should_return_nil_page_not_found_with_last(self):
    self.response.result = {'meta': {'links': {}}}
    next_response = self.pagination.last(self.response)
    assert next_response is None
