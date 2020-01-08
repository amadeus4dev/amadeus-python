from amadeus import Client, ResponseError

amadeus = Client()

print('Hotel Search')
try:
    # Get list of Hotels by city code
    r = amadeus.shopping.hotel_offers.get(cityCode='LON')
    print(r.data)
    # Get list of offers for a specific hotel
    r1 = amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'IALONCHO')
    # Confirm the availability of a specific offer
    r2 = amadeus.shopping.hotel_offer('D5BEE9D0D08B6678C2F5FAD910DC110BCDA187D21D4FCE68ED423426D0A246BB').get()
except ResponseError as error:
    print(error)
