from amadeus.client.decorator import Decorator


class BusiestPeriod(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of air traffic reports, based on number of travelers.

        .. code-block:: python

            amadeus.travel.analytics.air_traffic.busiest_period.get(
                cityCode='MAD',
                period='2017',
                direction=Direction.ARRIVING
            )

        :param cityCode: IATA code of the origin city, for
            example ``"BOS"`` for Boston.
        :param period: period when consumers are traveling
            in ``YYYY`` format
        :param direction: to select between
            arrivals and departures (default: arrivals)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/analytics/air-traffic/busiest-period',
                               **params)
