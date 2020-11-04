from amadeus.client.decorator import Decorator


class ItineraryPriceMetrics(Decorator, object):

    def get(self, **params):
        '''
        Returns itinerary price metrics by search criteria

        .. code-block:: python

            amadeus.analytics.itinerary_price_metrics.get(
                                            originIataCode='MAD',
                                            destinationIataCode='CDG',
                                            departureDate='2021-03-21')

        :param originIataCode: IATA code of the origin city, for
            example ``"BOS"`` for Boston.

        :param destinationIataCode: IATA code of the destination city,
            for example ``"ATH"`` for Athens.

        :param departureDate: scheduled departure date of the flight,
            local to the departure airport, format YYYY-MM-DD

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/analytics/itinerary-price-metrics', **params)
