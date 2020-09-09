from amadeus.client.decorator import Decorator


class Flights(Decorator, object):

    def get(self, **params):
        '''
        Retrieves a unique flight status by search criteria

        .. code-block:: python

            amadeus.schedule.flights.get(
                            carrierCode='AZ',
                            flightNumber='319',
                            scheduledDepartureDate='2021-03-13')

        :param carrierCode: the IATA carrier code

        :param flightNumber: flight number as assigned by the carrier

        :param scheduledDepartureDate: scheduled departure date of the flight,
            local to the departure airport, format YYYY-MM-DD

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/schedule/flights', **params)
