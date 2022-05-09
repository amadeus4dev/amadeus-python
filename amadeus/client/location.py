#
class Location(object):
    '''
    A list of location types, as used in searching for locations

    .. code-block:: python


        from amadeus import Location

        amadeus.reference_data.locations.get(
            keyword='lon',
            subType=Location.ANY
        )

    :cvar AIRPORT: ``"AIRPORT"``
    :cvar CITY: ``"CITY"``
    :cvar ANY: ``"AIRPORT,CITY"``
    '''
    # Airport
    AIRPORT = 'AIRPORT'
    # City
    CITY = 'CITY'
    # Any
    ANY = ','.join([AIRPORT, CITY])
