import pytest
import mock
from amadeus import Response, Request, Client
from amadeus import NetworkError, ServerError, AuthenticationError
from amadeus import NotFoundError, ClientError, ParserError


@pytest.fixture
def self():
    self.request = mock.MagicMock(Request)
    self.client = mock.MagicMock(Client)
    self.client.log_level = 'silent'
    return self


@pytest.fixture
def response_setup():
    http_response = mock.MagicMock()
    request = mock.MagicMock(Request)
    response_setup.client = mock.MagicMock(Client)
    response_setup.client.log_level = 'silent'
    response_setup.response = Response(http_response, request)
    return response_setup


def test_should_parse_body(self, response_setup):
    response_setup.response.status_code = '200'
    response_setup.response.headers = {'Content-Type': 'application/json'}
    response_setup.response.text = '{ "data" : { "a" : 1 } }'
    response = Response(response_setup.response, self.request)
    response = response._parse(response_setup.client)
    assert isinstance(response, Response)


def test_should_raise_network_error_with_no_code(response_setup):
    response_setup.response.status_code = None
    response_setup.response.parsed = False
    with pytest.raises(NetworkError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_server_error_with_500(response_setup):
    response_setup.response.status_code = 500
    response_setup.response.parsed = False
    with pytest.raises(ServerError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_auth_error_with_401(response_setup):
    response_setup.response.status_code = 401
    response_setup.response.parsed = False
    with pytest.raises(AuthenticationError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_not_found_error_with_404(response_setup):
    response_setup.response.status_code = 404
    response_setup.response.parsed = False
    with pytest.raises(NotFoundError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_a_generic_error_with_400(response_setup):
    response_setup.response.status_code = 400
    response_setup.response.parsed = False
    with pytest.raises(ClientError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_error_if_not_parsed_with_200(response_setup):
    response_setup.response.status_code = 200
    response_setup.response.parsed = False
    with pytest.raises(ParserError):
        response_setup.response._detect_error(response_setup.client)


def test_should_raise_error_when_exception(response_setup):
    response_setup.response.status_code = 200
    response_setup.response.parsed = True
    response_setup.response.body = None
    response_setup.response._detect_error(response_setup.client)


def test_should_not_raise_error_body_with_204(response_setup):
    response_setup.response.status_code = 204
    response_setup.response.parsed = False
    assert response_setup.response.status_code == 204
    response_setup.response._detect_error(response_setup.client)
