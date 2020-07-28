from amadeus.client.decorator import Decorator


class RecommendedLocations(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)

    def get(self, **params):
        '''
        Returns a list of destination recommendations

        .. code-block:: python


            client.reference_data.recommended_locations.get(
                cityCodes='PAR'
                travelerCountryCode='FR'
            )

        :param cityCodes: city used by the algorithm to recommend new destinations
            For example: ``PAR``
        :param travelerCountryCode: origin country following IATA standard
            For example: ``FR``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/recommended-locations', **params)
