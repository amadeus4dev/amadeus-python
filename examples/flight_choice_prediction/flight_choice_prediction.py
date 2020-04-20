from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find the probability of the flight MAD to NYC to be chosen
    '''
    result = amadeus.shopping.flight_offers_search.get(
            originLocationCode='MAD',
            destinationLocationCode='NYC',
            departureDate='2020-11-01',
            adults=1).result
    response = amadeus.shopping.flight_offers.prediction.post(result)
    # print(response.data)
except ResponseError as error:
    raise error
