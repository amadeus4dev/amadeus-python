import mock
from amadeus import Response


def test_response_init():
    http_response = mock.MagicMock()
    request = mock.MagicMock()
    response = Response(http_response, request)

    assert response.http_response == http_response
    assert response.request == request
