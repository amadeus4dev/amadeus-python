from amadeus.client.decorator import Decorator


class BySquare(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of activities
            around a defined square (4 points).

        .. code-block:: python


            client.shopping.activities.by_square.get(
                north=41.397158,
                west=2.160873,
                south=41.394582,
                east=2.177181
            )

        :param north: latitude north of bounding box.
            For example: ``41.397158``
        :param west: longitude west of bounding box.
            For example: ``2.160873``
        :param south: latitude south of bounding box.
            For example: ``41.394582``
        :param east: longitude east of bounding box.
            For example: ``2.177181``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/shopping/activities/by-square', **params)
