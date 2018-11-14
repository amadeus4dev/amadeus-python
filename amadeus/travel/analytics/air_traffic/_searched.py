from amadeus.client.decorator import Decorator


class Searched(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of air traffic reports, based on number of searches.

        .. code-block:: python

            amadeus.travel.analytics.air_traffic.searched.get(
                originCityCode='MAD',
                searchPeriod='2017-08',
                marketCountryCode='ES'
            )

        :param originCityCode: IATA code of the origin city, for
            example ``"MAD"`` for Madrid.
        :param searchPeriod: period when consumers are traveling
            in ``YYYY-MM`` format
        :param marketCountryCode: IATA code of the country from which
            searches were made - e.g. ``"ES"`` for Spain


        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/analytics/air-traffic/searched',
                               **params)
