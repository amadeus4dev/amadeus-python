from amadeus import Client, Location

class TestClient(object):
    def test__init__(self):
        assert Client is not None
        assert Location is not None
