from amadeus import Client, ResponseError

amadeus = Client()

print('Flight Delay Prediction')
try:
    '''
    Will there be a delay from BRU to FRA? If so how much delay?
    '''
    response = amadeus.travel.predictions.flight_delay.get(originLocationCode='BRU', destinationLocationCode='FRA',
                                                           departureDate='2020-11-14', departureTime='11:05:00',
                                                           arrivalDate='2020-11-14', arrivalTime='12:10:00',
                                                           aircraftCode='32A', carrierCode='LH',
                                                           flightNumber='1009', duration='PT1H05M')
    print(response.data)
except ResponseError as error:
    print(error)
