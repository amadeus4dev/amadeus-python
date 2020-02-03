from amadeus import Client, ResponseError
from amadeus import Location

amadeus = Client()

try:
    '''
    Which cities or airports start with 'r'?
    '''
    response = amadeus.reference_data.locations.get(keyword='r',
                                                    subType=Location.ANY)
    # print(response.data)
except ResponseError as error:
    raise error
