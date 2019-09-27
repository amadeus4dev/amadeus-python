from amadeus.client.decorator import Decorator


class TripPurpose(Decorator, object):
    def get(self, **params):
        '''
        Predicts traveler purpose, Business or Leisure,
        with the probability in the context of search & shopping

        .. code-block:: python

            amadeus.travel.predictions.trip_purpose.get(
                            originLocationCode='NYC',
                            destinationLocationCode='MAD',
                            departureDate='2020-08-01',
                            returnDate='2020-08-12',
                            searchDate='2020-06-11')

        :param originLocationCode: the City/Airport IATA code from which
            the flight will depart. ``"NYC"``, for example for New York

        :param destinationLocationCode: the City/Airport IATA code to which
            the flight is going. ``"MAD"``, for example for Madrid

        :param departureDate: the date on which to fly out, in `YYYY-MM-DD` format

        :param returnDate: the date on which the flight returns to the origin,
            in `YYYY-MM-DD` format

        :param searchDate: the date on which the traveler performs the search,
            in `YYYY-MM-DD` format.
            If it is not specified the current date will be used

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/predictions/trip-purpose', **params)
