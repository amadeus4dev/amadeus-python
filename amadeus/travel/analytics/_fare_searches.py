from amadeus.client.decorator import Decorator


class FareSearches(Decorator, object):
    def get(self, **params):
        '''
        The Fare Search History API allows to find the number of
        estimated searches from an origin, optionally a destination,
        within a time period when travelers are performing the searches.

        .. code-block:: python

            amadeus.travel.analytics.fare_searches.get(
                origin='LHR',
                sourceCountry='FR'
                period='2011'
            )

        :param cityCode: IATA code of the origin city, for
            example ``"BOS"`` for Boston.
        :param sourceCountry: IATA code of the country from which fare
            searches were made - e.g. ``"US"`` for United States
        :param period: period of search; can be a year
            or a month or a week. ISO format must be used - e.g. ``"2015"``
            for year; ``"2015-05"`` for month and ``"2015-W04"`` for week.
            Period ranges are not supported. Only periods from year
            ``"2011-01"`` up to current year and previous month or week
            are valid. Future dates are not supported.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/travel/analytics/fare-searches', **params)
