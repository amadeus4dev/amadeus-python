from amadeus.client.decorator import Decorator


class Activity(Decorator, object):
    def __init__(self, client, activity_id):
        Decorator.__init__(self, client)
        self.activity_id = activity_id

    def get(self, **params):
        '''
        Returns a single activity from a given id.

        .. code-block:: python

            client.shopping.activities('4615').get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/shopping/activities/{0}'
                               .format(self.activity_id), **params)
