from amadeus.client.decorator import Decorator


class TripPurpose(Decorator, object):
    def get(self, **params):
        '''
        Get forecast traveler purpose, Business or Leisure,
        together with the probability in the context of search & shopping

        .. code-block:: python

            amadeus.trip.trip_purpose_prediction.get(originLocationCode='XKPARC12',
            destinationLocationCode='XKPARC12',
            departureDate='XKPARC12', returnDate='XKPARC12',
            searchDate='XKPARC12')

        :param originLocationCode: Amadeus Property Code (8 chars), for
            example ``XKPARC12``.

        :param destinationLocationCode: the City/Airport IATA code from which
        the flight will
            depart. ``"MAD"``, for example for Madrid.

        :param departureDate: the City/Airport IATA code to which the flight is
            going. ``"BOS"``, for example for Boston.

        :param returnDate: the date on which to fly out, in `YYYY-MM-DD`
            format

        :param searchDate: the date on which to fly out, in `YYYY-MM-DD`
            format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/predictions/trip-purpose', **params)
