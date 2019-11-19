from amadeus.client.decorator import Decorator


class FlightDelay(Decorator, object):
    def get(self, **params):
        '''
        Forecast the chances for a flight to be delayed

        .. code-block:: python

        amadeus.travel.predictions.flight_delay.get(originLocationCode='BRU',
                                                           destinationLocationCode='FRA',
                                                           departureDate='2020-01-14',
                                                           departureTime='11:05:00',
                                                           arrivalDate='2020-01-14',
                                                           arrivalTime='12:10:00',
                                                           aircraftCode='32A',
                                                           carrierCode='LH',
                                                           flightNumber='1009',
                                                           duration='PT1H05M')

        :param originLocationCode: the City/Airport IATA code from which
            the flight will depart. ``"NYC"``, for example for New York

        :param destinationLocationCode: the City/Airport IATA code to which
            the flight is going. ``"MAD"``, for example for Madrid

        :param departureDate: the date on which the traveler departs
            from the origin, in `YYYY-MM-DD` format

        :param departureTime: local time on which to fly out,
            in `HH:MM:SS` format

        :param arrivalDate: the date on which the traveler arrives
            to the destination, in `YYYY-MM-DD` format

        :param arrivalTime: local time on which the traveler arrives
            to the destination, in `HH:MM:SS` format

        :param aircraftCode: IATA aircraft code

        :param carrierCode: airline / carrier code

        :param flightNumber: flight number as assigned by the carrier

        :param duration: flight duration,
            in `PnYnMnDTnHnMnS` format e.g. PT2H10M

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/travel/predictions/flight-delay', **params)
