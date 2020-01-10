from amadeus import Client, ResponseError

amadeus = Client()

print('Flight Most Booked Destinations')
try:
    '''
    Where were people flying to from Madrid in the August 2017?
    '''
    response = amadeus.travel.analytics.air_traffic.booked.get(originCityCode='MAD', period='2017-08')
    print(response.data)
except ResponseError as error:
    print(error)
