from amadeus import Client, ResponseError

amadeus = Client()

print('Flight Offers Search')
try:
    '''
    Confirm availability and price from SYD to BKK in summer 2020
    '''
    flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
                                                        departureDate='2020-07-01', adults=1).data
    response = amadeus.shopping.flight_offers.pricing.post(flights[0])
    print(response.data)
except ResponseError as error:
    print(error)
