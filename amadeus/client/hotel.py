#
class Hotel(object):
    '''
    A list of hotel sub types, as used in Hotel Name Autocomplete

    .. code-block:: python


        from amadeus import Hotel

        amadeus.reference_data.locations.hotel.get(
            keyword='PARI',
            subType=[Hotel.HOTEL_LEISURE, Hotel.HOTEL_GDS]
        )

    :cvar HOTEL_LEISURE: ``"HOTEL_LEISURE"``
    :cvar HOTEL_GDS: ``"HOTEL_GDS"``
    '''
    # Hotel Leisure
    HOTEL_LEISURE = 'HOTEL_LEISURE'
    # Hotel GDS
    HOTEL_GDS = 'HOTEL_GDS'
