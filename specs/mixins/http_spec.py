import pytest
import mock
import unittest.mock
from amadeus import Client, Response, ResponseError
from urllib.error import URLError


@pytest.fixture
def self():
    self = mock.MagicMock()
    self.client = Client(client_id='123', client_secret='234', log_level='silent')
    self.response = Response(None, None)
    self.request_method = mock.MagicMock(return_value=self.response)
    return self


def test_client_get(self):
    self.client.request = self.request_method
    response = self.client.get('/foo', foo='bar')
    assert response == self.response
    self.client.request.assert_called_with('GET', '/foo', {'foo': 'bar'})


def test_client_delete(self):
    self.client.request = self.request_method
    response = self.client.delete('/foo', foo='bar')
    assert response == self.response
    self.client.request.assert_called_with(
        'DELETE', '/foo', {'foo': 'bar'})


def test_client_post(self):
    self.client.request = self.request_method
    response = self.client.post('/foo', {'foo': 'bar'})
    assert response == self.response
    self.client.request.assert_called_with('POST', '/foo', {'foo': 'bar'})


def test_client_request(self):
    self.response.result = {'access_token': '123'}
    self.client._unauthenticated_request = self.request_method
    response = self.client.request('POST', '/foo', {'foo': 'bar'})
    assert response == self.response
    assert self.client._unauthenticated_request.call_args == mock.call(
            'POST', '/foo', {'foo': 'bar'}, 'Bearer 123'
    )


def test_client_request_use_same_access_token(self):
    self.response.result = {'access_token': '123', 'expires_in': 2000}
    self.client._unauthenticated_request = self.request_method
    self.client.request('POST', '/foo', {'foo': 'bar'})

    self.response.result = {'access_token': '234', 'expires_in': 2000}
    self.client._unauthenticated_request = self.request_method
    self.client.request('POST', '/foo', {'foo': 'bar'})
    assert not self.client._unauthenticated_request.assert_called_with(
        'POST', '/foo', {'foo': 'bar'}, 'Bearer 123')


def test_unauthenticated_request(self):
    http_response = mock.MagicMock()
    http_response.code = 200
    http_response.getheaders.return_value = [('Content-Type', 'application/json')]
    http_response.read.return_value = '{ "data" : { "a" : 1 } }'

    # Patch the client's `http` method to return the mock HTTP response
    unittest.mock.patch.object(self.client, 'http', return_value=http_response)

    # Test the client's _unauthenticated_request method
    with pytest.raises(ResponseError):
        response = self.client._unauthenticated_request('GET', '/foo', {}, None)
        assert self.client.call_count == 1
        assert response == http_response

    # Test that a HTTPError is caught
    self.client.http.side_effect = URLError('Error')
    with pytest.raises(ResponseError):
        self.client._unauthenticated_request('GET', '/foo', {}, None)

    # Test logging in debug mode
    with mock.patch.object(self.client, 'http', return_value=http_response):
        logger = mock.MagicMock()
        self.client.logger = logger
        self.client.log_level = 'debug'
        with pytest.raises(ResponseError):
            response = self.client._unauthenticated_request(
                'GET', '/foo', {}, None)
            assert logger.debug.call_count == 2
