from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find cheapest destinations from Madrid
    '''
    response = amadeus.shopping.flight_destinations.get(origin='MAD')
    # print(response.data)
except ResponseError as error:
    raise error
