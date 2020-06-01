from amadeus.client.decorator import Decorator


class SafetyRatedLocation(Decorator, object):
    def __init__(self, client, safety_id):
        Decorator.__init__(self, client)
        self.safety_id = safety_id

    def get(self, **params):
        '''
        Returns safety information of a location by its Id.

        .. code-block:: python

            amadeus.safety.safety_rated_location('Q930400801').get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/safety/safety-rated-locations/{0}'
                               .format(self.safety_id), **params)
