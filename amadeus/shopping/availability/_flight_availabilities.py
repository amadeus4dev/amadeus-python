from amadeus.client.decorator import Decorator


class FlightAvailabilities(Decorator, object):
    def post(self, body):
        '''
        Get available seats in different fare classes

        .. code-block:: python

            amadeus.shopping.availability.flight_availabilities.post(body)

        :param body: the parameters to send to the API

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.post(
            '/v1/shopping/availability/flight-availabilities', body)
