from amadeus.client.decorator import Decorator


class PointOfInterest(Decorator, object):
    def __init__(self, client, poi_id):
        Decorator.__init__(self, client)
        self.poi_id = poi_id

    def get(self, **params):
        '''
        Returns a single Point of Interest from a given id.

        .. code-block:: python

            amadeus.reference_data.locations.point_of_interest('9CB40CB5D0').get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/reference-data/locations/pois/{0}'
                               .format(self.poi_id), **params)
