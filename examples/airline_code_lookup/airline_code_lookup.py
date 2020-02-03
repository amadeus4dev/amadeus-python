from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What's the airline name for the IATA code BA?
    '''
    response = amadeus.reference_data.airlines.get(airlineCodes='BA')
    # print(response.data)
except ResponseError as error:
    raise error
