from amadeus.client.decorator import Decorator
from .analytics import CategoryRatedAreas


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.category_rated_areas = CategoryRatedAreas(client)
