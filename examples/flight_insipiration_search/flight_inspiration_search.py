from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find cheapest destinations from Boston
    '''
    response = amadeus.shopping.flight_destinations.get(origin='BOS')
    # print(response.data)
except ResponseError as error:
    raise error
