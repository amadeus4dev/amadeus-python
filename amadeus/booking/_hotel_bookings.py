from amadeus.client.decorator import Decorator


class HotelBookings(Decorator, object):
    def post(self, hotel_offer_id, guests, payment):
        '''
        Books a hotel

        .. code-block:: python

            amadeus.booking.hotel_bookings.post(hotel_offer_id, guests, payment)

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        guests_info = []
        payment_info = []
        if type(guests) is not list:
            guests_info.append(guests)
        else:
            guests_info.extend(guests)
        body = {'data': {'offerId': hotel_offer_id,
                         'guests': guests_info,
                         'payment': payment_info}}
        return self.client.post('/v1/booking/hotel-bookings', body)
