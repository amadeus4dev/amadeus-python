from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find cheapest dates from Madrid to London
    '''
    response = amadeus.shopping.flight_dates.get(origin='MAD', destination='LON')
    # print(response.data)
except ResponseError as error:
    raise error
