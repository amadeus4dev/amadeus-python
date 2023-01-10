import pytest
import mock
from amadeus import Client
from amadeus.client.access_token import AccessToken


class TokenResponse:
    def __init__(self, result):
        self.result = result


@pytest.fixture
def self():
    self.request = mock.MagicMock(
        return_value=TokenResponse({'access_token': 'abc', 'expires_in': 1799}))
    self.client = mock.MagicMock(Client)
    self.client._unauthenticated_request = self.request
    self.client.client_id = '123'
    self.client.client_secret = '234'
    self.access_token = AccessToken(self.client)
    return self


def test_bearer_token(self):
    token = self.access_token._bearer_token()
    assert token == 'Bearer abc'
    self.client._unauthenticated_request.assert_called_with(
        'POST', '/v1/security/oauth2/token',
        {
            'grant_type': 'client_credentials',
            'client_id': '123',
            'client_secret': '234'
        })


def test_cached_token_valid(self):
    access_token = self.access_token
    token = access_token._bearer_token()
    assert token == 'Bearer abc'
    self.client._unauthenticated_request.assert_called_once()
    token2 = access_token._bearer_token()
    assert token2 == 'Bearer abc'
    self.client._unauthenticated_request.assert_called_once()


def test_cached_token_expired(self):
    access_token = self.access_token
    token = access_token._bearer_token()
    assert token == 'Bearer abc'
    access_token.expires_at = 0
    token2 = access_token._bearer_token()
    assert token2 == 'Bearer abc'
    assert self.client._unauthenticated_request.call_count == 2
