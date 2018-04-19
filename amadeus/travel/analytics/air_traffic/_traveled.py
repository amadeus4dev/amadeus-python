from amadeus.client.decorator import Decorator


class Traveled(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of air traffic reports.

        .. code-block:: python

            amadeus.travel.analytics.air_traffic.traveled.get(
                origin='LHR',
                period='2011-01'
            )

        :param cityCode: IATA code of the origin city, for
            example ``"BOS"`` for Boston.
        :param query: period when consumers are traveling
            in ``YYYY-MM`` format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/travel/analytics/air-traffic/traveled', **params)
