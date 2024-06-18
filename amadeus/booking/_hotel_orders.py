from amadeus.client.decorator import Decorator


class HotelOrders(Decorator, object):
    def post(self,
             guests,
             travel_agent,
             room_associations=[],
             payment={},
             arrival_information={}):
        '''
        Book hotel(s) via Hotel Booking API V2

        .. code-block:: python

            amadeus.booking.hotel_orders.post(guests,
                                              travel_agent,
                                              room_associations,
                                              payment,
                                              arrival_information)

        The parameters guests and room_associations can be passed as dictionary
        or list of dictionaries. If they are dictionary in this method they are
        converted to a list of dictionaries.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        guests_info = []
        room_associations_info = []
        if not isinstance(guests, list):
            guests_info.append(guests)
        else:
            guests_info.extend(guests)
        if not isinstance(room_associations, list):
            room_associations_info.append(room_associations)
        else:
            room_associations_info.extend(room_associations)
        body = {'data': {'type': 'hotel-order',
                         'guests': guests_info,
                         'travelAgent': travel_agent,
                         'roomAssociations': room_associations_info,
                         'arrivalInformation': arrival_information,
                         'payment': payment}}
        return self.client.post('/v2/booking/hotel-orders', body)
