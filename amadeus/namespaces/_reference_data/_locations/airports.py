from amadeus.client.decorator import Decorator


class Airports(Decorator, object):
    def get(self, **params):
        return self.client.get(
            '/v1/reference-data/locations/airports', **params)
