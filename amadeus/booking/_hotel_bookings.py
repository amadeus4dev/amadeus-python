from amadeus.client.decorator import Decorator


class HotelBookings(Decorator, object):
    def post(self, hotel_offer_id, guests, payments):
        '''
        Books a hotel

        .. code-block:: python

            amadeus.booking.hotel_bookings.post(hotel_offer_id, guests, payments)

        The parameters guests and payments can be passed as dictionary
        or list of dictionaries. If they are dictionary in this method they are
        converted to a list of dictionaries.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        guests_info = []
        payment_info = []
        if not isinstance(guests, list):
            guests_info.append(guests)
        else:
            guests_info.extend(guests)
        if not isinstance(payments, list):
            payment_info.append(payments)
        else:
            payment_info.extend(payments)
        body = {'data': {'offerId': hotel_offer_id,
                         'guests': guests_info,
                         'payments': payment_info}}
        return self.client.post('/v1/booking/hotel-bookings', body)
