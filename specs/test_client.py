from amadeus import Client, Location


def test_client_exists():
    assert Client is not None


def test_client_has_helper_locations():
    assert Location is not None
    assert Location.ANY == 'AIRPORT,CITY'
