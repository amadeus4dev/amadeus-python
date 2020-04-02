from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find cheapest dates from Boston to San Francisco
    '''
    response = amadeus.shopping.flight_dates.get(origin='BOS', destination='SFO')
    # print(response.data)
except ResponseError as error:
    raise error
