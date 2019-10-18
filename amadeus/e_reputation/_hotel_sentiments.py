from amadeus.client.decorator import Decorator


class HotelSentiments(Decorator, object):
    def get(self, **params):
        '''
        Provides ratings and sentiments scores for hotels

        .. code-block:: python

            amadeus.e_reputation.hotel_sentiments.get(hotelIds='TELONMFS,ADNYCCTB'])

        :param hotelIds: comma separated string list of amadeus hotel Ids (max
        3). These Ids are found in the Hotel Search response. ``"RDLON308"``,
        for example for the Radisson Blu Hampshire hotel.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/e-reputation/hotel-sentiments', **params)
