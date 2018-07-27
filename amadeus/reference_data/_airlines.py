from amadeus.client.decorator import Decorator


class Airlines(Decorator, object):
    def get(self, **params):
        '''
        Returns the name of the airline given an IATA code.

        .. code-block:: python

            amadeus.reference_data.airlines.get(IATACode='U2')

        :param IATACode: the IATA code for the airline, e.g. ``"1X"``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/reference-data/airlines', **params)
