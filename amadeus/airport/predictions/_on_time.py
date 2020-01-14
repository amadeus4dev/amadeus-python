from amadeus.client.decorator import Decorator


class AirportOnTime(Decorator, object):
    def get(self, **params):
        '''
        Returns a percentage of on-time flight departures

        .. code-block:: python

            amadeus.airport.predictions.on_time.get(
                            airportCode='JFK',
                            date='2020-09-01')

        :param airportCode: the City/Airport IATA code from which
            the flight will depart. ``"NYC"``, for example for New York

        :param date: the date on which to fly out, in `YYYY-MM-DD` format

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/airport/predictions/on-time', **params)
