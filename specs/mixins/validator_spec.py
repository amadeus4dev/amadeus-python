

from amadeus import Client
from os import environ
from logging import Logger, getLogger
import pytest
from mock import MagicMock


@pytest.fixture
def valid_params():
    return {
        'client_id': '1234',
        'client_secret': '4546'
    }


def test_client_init(valid_params):
    client = Client(**valid_params)
    assert isinstance(client, Client)


def test_client_init_with_env_vars(valid_params):
    environ['AMADEUS_CLIENT_ID'] = '123'
    environ['AMADEUS_CLIENT_SECRET'] = '234'

    client = Client()
    assert isinstance(client, Client)

    del environ['AMADEUS_CLIENT_ID']
    del environ['AMADEUS_CLIENT_SECRET']


def test_client_init_with_missing_params(valid_params):
    # Test missing client_id
    valid_params_copy = valid_params.copy()
    del valid_params_copy['client_id']
    with pytest.raises(ValueError):
        Client(**valid_params_copy)

    # Test missing client_secret
    valid_params_copy = valid_params.copy()
    del valid_params_copy['client_secret']
    with pytest.raises(ValueError):
        Client(**valid_params_copy)


def test_client_logging(valid_params):
    # Test default logger
    amadeus = Client(**valid_params)
    assert isinstance(amadeus.logger, Logger)
    assert amadeus.log_level == 'silent'

    # Test custom logger
    logger = getLogger('amadeus')
    valid_params['logger'] = logger
    amadeus = Client(**valid_params)
    assert amadeus.logger is logger
    assert amadeus.log_level == 'silent'

    # Test custom log level
    logger.setLevel(10)
    amadeus = Client(**valid_params)
    assert amadeus.logger is logger
    assert amadeus.logger.level == 10


def test_client_options(valid_params):
    # Test unrecognized option warning
    logger = MagicMock()
    valid_params['logger'] = logger
    valid_params['foobar'] = 'test'
    Client(**valid_params)
    logger.warning.assert_called_with('Unrecognized option: foobar')

    # Test default host
    amadeus = Client(**valid_params)
    assert amadeus.host == Client.HOSTS['test']

    # Test custom hostname
    valid_params['hostname'] = 'production'
    amadeus = Client(**valid_params)
    assert amadeus.host == Client.HOSTS['production']

    # Test custom host
    host = 'http://foo.bar.com/'
    valid_params['host'] = host
    amadeus = Client(**valid_params)
    assert amadeus.host == host
