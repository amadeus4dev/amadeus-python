from amadeus.client.decorator import Decorator


class SearchedByDestination(Decorator, object):
    def get(self, **params):
        '''
        The Flight Most Searched Destinations API allows to find the number of
        estimated searches from an origin and a destination,
        within a time period when travelers are performing the searches.

        .. code-block:: python

            amadeus.travel.analytics.air_traffic.searched_by_destination.get(
                originCityCode='MAD',
                destinationCityCode='NYC',
                marketCountryCode='ES'
                searchPeriod='2017-08'
            )

        :param originCityCode: IATA code of the origin city, for
            example ``"MAD"`` for Madrid.
        :param destinationCityCode: IATA code of the destination city, for
            example ``"NYC"`` for New-York.
        :param marketCountryCode: IATA code of the country from which
            searches were made - e.g. ``"ES"`` for Spain
        :param searchPeriod: period when consumers are traveling
            in ``YYYY-MM`` format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/travel/analytics/air-traffic/searched/by-destination', **params)
