from amadeus.client.decorator import Decorator


class AirTraffics(Decorator, object):
    def get(self, **params):
        return self.client.get(
            '/v1/travel/analytics/air-traffics', **params)
