from amadeus import Client, ResponseError
import sys
amadeus = Client()

try:
    '''
    Find the cheapest flights from SYD to BKK
    '''
    response = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2020-07-01', adults=1)
    # print(response.data)
except ResponseError as error:
    print(error)
    sys.exit(1)
