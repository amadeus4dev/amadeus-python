from amadeus import Client, ResponseError

amadeus = Client()

try:
    # Get list of Hotels by city code
    hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode='LON')
    # print(hotels_by_city.data)
    # Get list of offers for a specific hotel
    hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'BGLONBGB')
    # print(hotel_offers.data)
    # Confirm the availability of a specific offer
    # print(hotel_offers.data)
    offer_availability = amadeus.shopping.hotel_offer(hotel_offers.data['offers'][0]['id']).get()
    # print(offer_availability.data)
    guests = [{'id': 1, 'name': { 'title': 'MR', 'firstName': 'BOB', 'lastName': 'SMITH' }, 'contact': { 'phone': '+33679278416', 'email': 'bob.smith@email.com'}}]
    payments = [ { 'id': 1, 'method': 'creditCard', 'card': { 'vendorCode': 'VI', 'cardNumber': '4151289722471370', 'expiryDate': '2021-08' } } ]
    amadeus.booking.hotel_bookings.post(offer_availability, guests, payments)

except ResponseError as error:
    raise error
