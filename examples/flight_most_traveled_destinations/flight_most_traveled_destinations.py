from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Where were people flying to from Madrid in the January 2017?
    '''
    response = amadeus.travel.analytics.air_traffic.traveled.get(originCityCode='MAD', period='2017-01')
    # print(response.data)
except ResponseError as error:
    raise error
