from amadeus import Client, ResponseError

amadeus = Client()

traveler = { 'id': '1', 'dateOfBirth': '1982-01-16', 'name': { 'firstName': 'JORGE', 'lastName': 'GONZALES' }, 'gender': 'MALE', 'contact': { 'emailAddress': 'jorge.gonzales833@telefonica.es', 'phones': [ { 'deviceType': 'MOBILE', 'countryCallingCode': '34', 'number': '480080076' } ] }, 'documents': [ { 'documentType': 'PASSPORT', 'birthPlace': 'Madrid', 'issuanceLocation': 'Madrid', 'issuanceDate': '2015-04-14', 'number': '00000000', 'expiryDate': '2025-04-14', 'issuanceCountry': 'ES', 'validityCountry': 'ES', 'nationality': 'ES', 'holder': True } ] }

try:
    flight_search = amadeus.shopping.flight_offers_search.get(originLocationCode='MAD', destinationLocationCode='ATH', departureDate='2020-12-01', adults=1).data
    price_confirm = amadeus.shopping.flight_offers.pricing.post(flight_search[0]).data
    booked_flight = amadeus.booking.flight_orders.post(flight_search[0], traveler).data
    updated_booking = amadeus.booking.flight_order(booked_flight['id']).get()
except ResponseError as error:
    pass