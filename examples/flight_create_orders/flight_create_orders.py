from amadeus import Client, ResponseError

amadeus = Client()

traveler = {
  'id': '1',
  'dateOfBirth': '1982-01-16',
  'name': {
    'firstName': 'JORGE',
    'lastName': 'GONZALES'
  },
  'gender': 'MALE',
  'contact': {
    'emailAddress': 'jorge.gonzales833@telefonica.es',
    'phones': [{
      'deviceType': 'MOBILE',
      'countryCallingCode': '34',
      'number': '480080076'
    }]
  },
  'documents': [{
    'documentType': 'PASSPORT',
    'birthPlace': 'Madrid',
    'issuanceLocation': 'Madrid',
    'issuanceDate': '2015-04-14',
    'number': '00000000',
    'expiryDate': '2025-04-14',
    'issuanceCountry': 'ES',
    'validityCountry': 'ES',
    'nationality': 'ES',
    'holder': True
  }]
}

try:
    # Flight Offers Search to search for flights from MAD to ATH
    # print('Flight Offers Search')
    flight_search = amadeus.shopping.flight_offers_search.get(originLocationCode='MAD',
                                                              destinationLocationCode='ATH',
                                                              departureDate='2020-12-01',
                                                              adults=1).data
    # Flight Offers Price to confirm the price of the chosen flight
    # print('Flight Offers Price')
    price_confirm = amadeus.shopping.flight_offers.pricing.post(flight_search[0]).data
    # Flight Create Orders to book the flight
    # print('Flight Create Orders')
    booked_flight = amadeus.booking.flight_orders.post(flight_search[0], traveler).data
    # Flight Order Management returns the last-updated version of the booking
    # print('Flight Order Management')
    updated_booking = amadeus.booking.flight_order(booked_flight['id']).get()
    updated_booking = amadeus.booking.flight_order(booked_flight['id']).delete()
except ResponseError as error:
    # print(error.response.body)
    pass
