from amadeus.client.decorator import Decorator


class Airlines(Decorator, object):
    def get(self, **params):
        '''
        Returns the name of the airline given an IATA code.

        .. code-block:: python

            amadeus.reference_data.airlines.get(airlineCodes='U2')

        :param airlineCodes: the IATA or ICAO code for the airline, e.g.
        :``"AF"`` (Air France IATA code)
        :or ``"AFR"`` (Air France ICAO code)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/reference-data/airlines', **params)
