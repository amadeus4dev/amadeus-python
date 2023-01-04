from mock import MagicMock
from unittest.mock import Mock

from amadeus import NetworkError, Response, Client


def test_ResponseError_str_representation():
    # Test str(error) with no response present
    error = NetworkError(None)
    assert str(error) == '[---]'

    # Test str(error) with no data present
    response = Mock(Response)
    response.parsed = True
    response.result = {}
    response.status_code = 400

    error = NetworkError(response)
    assert str(error) == '[400]'

    # Test str(error) with errors present
    response = Mock(Response)
    response.parsed = True
    response.result = {
        'errors': [
            {
                'detail': 'This field must be filled.',
                'source': {'parameter': 'departureDate'},
            },
            {
                'detail': 'This field must be filled.',
                'source': {'parameter': 'origin'},
            },
            {
                'detail': 'This field must be filled.',
                'source': {'parameter': 'destination'},
            },
        ]
    }
    response.status_code = 401

    error = NetworkError(response)
    error = NetworkError(response)
    assert (
        ('''[401]
[departureDate] This field must be filled.
[origin] This field must be filled.
[destination] This field must be filled.''')
    )

    # Test str(error) with error_description present
    response = Mock(Response)
    response.parsed = True
    response.result = {'error_description': 'error'}
    response.status_code = 401

    error = NetworkError(response)
    assert str(error) == '[401]\nerror'


def test_ResponseError_code():
    # Test .code with no response present
    error = NetworkError(None)
    assert error.code == 'NetworkError'


def test_ResponseError_log():
    # Test .log with log level set to 'warn'
    client = Mock(Client)
    client.logger = MagicMock()
    client.log_level = 'warn'

    error = NetworkError(None)
    error.code = 'Foo'
    error.description = 'Bar'
    error._log(client)

    assert client.logger.warning.called_with('Amadeus %s: %s', 'Foo', 'Bar')

    # Test .log with log level set to 'silent'
    client = Mock(Client)
    client.logger = MagicMock()
    client.log_level = 'silent'

    error = NetworkError(None)
    error._log(client)

    assert not client.logger.warning.called
