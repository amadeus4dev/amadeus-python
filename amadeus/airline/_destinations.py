from amadeus.client.decorator import Decorator


class Destinations(Decorator, object):
    def get(self, **params):
        '''
        Get airline destinations.

        .. code-block:: python

            amadeus.airline.destinations.get(airlineCode='BA')

        :param airlineCode: the airline code following IATA standard.
            Example: ``"BA"``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/airline/destinations', **params)
