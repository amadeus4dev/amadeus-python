from amadeus.client.decorator import Decorator


class Cities(Decorator, object):
    def get(self, **params):
        '''
        Returns cities that match a specific word or letters.

        .. code-block:: python


            amadeus.reference_data.locations.cities.get(
                keyword='PARI'
            )

        :param keyword: location query keyword.
            For example: ``PARI``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/locations/cities', **params)
