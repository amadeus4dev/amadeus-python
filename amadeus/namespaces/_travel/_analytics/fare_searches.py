from amadeus.client.decorator import Decorator


class FareSearches(Decorator, object):
    def get(self, **params):
        return self.client.get(
            '/v1/travel/analytics/fare-searches', **params)
