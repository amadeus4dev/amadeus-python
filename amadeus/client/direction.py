#
class Direction (object):
    '''
    A list of direction types, as used in Busiest Travel Period

    .. code-block:: python


        from amadeus import Direction

        client.travel.analytics.air_traffic.busiest_period.get(
            cityCode = 'MAD',
            period = '2017',
            direction = Direction.ARRIVING
        )

    :cvar ARRIVING: ``"ARRIVING"``
    :cvar DEPARTING: ``"DEPARTING"``
    '''
    # Arriving
    ARRIVING = 'ARRIVING'
    # Departing
    DEPARTING = 'DEPARTING'
