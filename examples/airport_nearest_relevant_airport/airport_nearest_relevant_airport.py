from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What relevant airports are there around a specific location?
    '''
    response = amadeus.reference_data.locations.airports.get(longitude=49.000, latitude=2.55)
    # print(response.data)
except ResponseError as error:
    raise error
