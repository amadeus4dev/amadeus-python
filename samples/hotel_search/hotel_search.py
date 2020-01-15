from amadeus import Client, ResponseError

amadeus = Client()

print('Hotel Search')
try:
    # Get list of Hotels by city code
    hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode='LON')
    print(hotels_by_city.data)
    # Get list of offers for a specific hotel
    hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'IALONCHO')
    print(hotel_offers.data)
    # Confirm the availability of a specific offer
    offer_availability = amadeus.shopping.hotel_offer('D5BEE9D0D08B6678C2F5FAD910DC110BCDA187D21D4FCE68ED423426D0A246BB').get()
    print(offer_availability.data)

except ResponseError as error:
    raise error
