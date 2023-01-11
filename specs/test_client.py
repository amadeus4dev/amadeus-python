from amadeus import Client, Location, Hotel


def test_client_exists():
    assert Client is not None


def test_client_has_helper_locations():
    assert Location is not None
    assert Location.ANY == 'AIRPORT,CITY'


def test_client_has_helper_hotels():
    assert Hotel is not None
    assert Hotel.HOTEL_GDS == 'HOTEL_GDS'
    assert Hotel.HOTEL_LEISURE == 'HOTEL_LEISURE'
