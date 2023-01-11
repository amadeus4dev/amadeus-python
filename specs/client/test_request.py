import pytest
from amadeus import Request
from urllib.request import Request as HTTPRequest


@pytest.fixture
def self():
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
    return self


def test_init(self):
    assert self.request.host == self.host
    assert self.request.port == self.port
    assert self.request.ssl is True
    assert self.request.scheme == 'https'
    assert self.request.verb == self.verb
    assert self.request.path == self.path
    assert self.request.params == self.params
    assert self.request.bearer_token == self.bearer_token
    assert self.request.client_version == self.client_version
    assert self.request.language_version == self.lang_version
    assert self.request.app_id == self.app_id
    assert self.request.app_version == self.app_version


def test_http_request(self):
    assert isinstance(self.request.http_request, HTTPRequest)
    assert self.request.http_request.data is None
    assert self.request.http_request.get_header('Content-Type', None) is None
    assert self.request.http_request.get_header(
        'Authorization') == self.bearer_token
    assert self.request.http_request.get_header(
        'Accept') == 'application/json, application/vnd.amadeus+json'
    assert self.request.http_request.get_header(
        'User-agent') == 'amadeus-python/1.2.3 python/2.3.4 amadeus-cli/3.4.5'

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
    assert isinstance(self.request.http_request, HTTPRequest)
    url = self.request.http_request.get_full_url()
    assert url == 'https://example.com/foo/bar'
    assert self.request.http_request.data == b'{\"foo\": \"bar\"}'


def test_x_http_method_override(self):
    for path in Request.list_httpoverride:
        self.request = Request({
                    'host': self.host,
                    'verb': 'POST',
                    'path': path,
                    'params': self.params,
                    'bearer_token': self.bearer_token,
                    'client_version': self.client_version,
                    'language_version': self.lang_version,
                    'app_id': self.app_id,
                    'app_version': self.app_version,
                    'port': self.port,
                    'ssl': self.ssl
                })
        assert isinstance(self.request.http_request, HTTPRequest)
        assert self.request.headers['X-HTTP-Method-Override'] == 'GET'


def test_custom_scheme_and_port(self):
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
    url = self.request.http_request.get_full_url()
    assert url == 'http://example.com:8080/foo/bar'
