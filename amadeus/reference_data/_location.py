from amadeus.client.decorator import Decorator


class Location(Decorator, object):
    def __init__(self, client, location_id):
        Decorator.__init__(self, client)
        self.location_id = location_id

    def get(self, **params):
        return self.client.get(
            '/v1/reference-data/locations/{0}'.format(self.location_id),
            **params
        )
