from amadeus.client.decorator import Decorator


class CheckinLinks(Decorator, object):
    def get(self, **params):
        return self.client.get(
            '/v2/reference-data/urls/checkin-links', **params)
