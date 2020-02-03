from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Find the probability of the flight MAD to NYC to be chosen
    '''
    result = amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC',
                                                departureDate='2020-10-01').result
    response = amadeus.shopping.flight_offers.prediction.post(result)
    # print(response.data)
except ResponseError as error:
    raise error
