from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Will there be a delay in the JFK airport on the 1st of September?
    '''
    response = amadeus.airport.predictions.on_time.get(airportCode='JFK', date='2020-09-01')
    # print(response.data)
except ResponseError as error:
    raise error
