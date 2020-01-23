from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What travelers think about this hotel?
    '''
    response = amadeus.e_reputation.hotel_sentiments.get(hotelIds = 'ADNYCCTB')
    # print(response.data)
except ResponseError as error:
    raise error
