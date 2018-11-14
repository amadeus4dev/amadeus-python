from amadeus.client.decorator import Decorator


class Traveled(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of air traffic reports, based on number of travelers.

        .. code-block:: python

            amadeus.travel.analytics.air_traffic.traveled.get(
                originCityCode='LHR',
                period='2017-01'
            )

        :param originCityCode: IATA code of the origin city, for
            example ``"BOS"`` for Boston.
        :param period: period when consumers are traveling
            in ``YYYY-MM`` format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/analytics/air-traffic/traveled',
                               **params)
