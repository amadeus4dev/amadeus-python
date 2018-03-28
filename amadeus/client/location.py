# A list of location types, as used in searching for locations
class Location(object):
    # Airport
    AIRPORT = 'AIRPORT'
    # City
    CITY = 'CITY'
    # Any
    ANY = ','.join([AIRPORT, CITY])
