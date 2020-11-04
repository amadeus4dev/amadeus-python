from mamba import description, it, before, context
from expects import expect, be_none
from doublex import method_returning
from doublex_expects import have_been_called_with

from amadeus import Client

with description('Namespaces') as self:
    with before.all:
        self.client = Client(
            client_id='123',
            client_secret='234'
        )

    with it('should define all expected paths'):
        client = self.client
        expect(client.reference_data).not_to(be_none)
        expect(client.reference_data.urls).not_to(be_none)
        expect(client.reference_data.urls.checkin_links).not_to(be_none)
        expect(client.reference_data.location).not_to(be_none)
        expect(client.reference_data.locations).not_to(be_none)
        expect(client.reference_data.locations.airports).not_to(be_none)
        expect(client.reference_data.locations.points_of_interest).not_to(be_none)
        expect(
            client.reference_data.locations.points_of_interest.by_square).not_to(
            be_none)
        expect(client.reference_data.locations.point_of_interest).not_to(be_none)
        expect(client.travel).not_to(be_none)
        expect(client.travel.analytics).not_to(be_none)
        expect(client.travel.analytics.air_traffic.traveled).not_to(be_none)
        expect(client.travel.analytics.air_traffic.booked).not_to(be_none)
        expect(client.travel.analytics.air_traffic.busiest_period).not_to(be_none)

        expect(client.travel.predictions).not_to(be_none)
        expect(client.travel.predictions.trip_purpose).not_to(be_none)
        expect(client.travel.predictions.flight_delay).not_to(be_none)

        expect(client.shopping).not_to(be_none)
        expect(client.shopping.flight_dates).not_to(be_none)
        expect(client.shopping.flight_destinations).not_to(be_none)
        expect(client.shopping.flight_offers).not_to(be_none)
        expect(client.shopping.flight_offers_search).not_to(be_none)
        expect(client.shopping.flight_offers.pricing).not_to(be_none)

        expect(client.shopping.seatmaps).not_to(be_none)

        expect(client.shopping.hotel_offers).not_to(be_none)
        expect(client.shopping.hotel_offer).not_to(be_none)
        expect(client.shopping.hotel_offers_by_hotel).not_to(be_none)

        expect(client.shopping.activities).not_to(be_none)

        expect(client.e_reputation.hotel_sentiments).not_to(be_none)

        expect(client.airport).not_to(be_none)
        expect(client.airport.predictions).not_to(be_none)
        expect(client.airport.predictions.on_time).not_to(be_none)

        expect(client.media).not_to(be_none)
        expect(client.media.files).not_to(be_none)
        expect(client.media.files.generated_photos).not_to(be_none)

        expect(client.travel.trip_parser_jobs).not_to(be_none)
        expect(client.travel.trip_parser_jobs.status).not_to(be_none)
        expect(client.travel.trip_parser_jobs.result).not_to(be_none)

        expect(client.travel.from_file).not_to(be_none)
        expect(client.travel.from_base64).not_to(be_none)

        expect(client.booking.flight_orders).not_to(be_none)
        expect(client.booking.flight_order).not_to(be_none)

        expect(client.safety.safety_rated_locations).not_to(be_none)
        expect(client.safety.safety_rated_locations.by_square).not_to(be_none)
        expect(client.safety.safety_rated_location).not_to(be_none)

        expect(client.schedule).not_to(be_none)
        expect(client.schedule.flights).not_to(be_none)

        expect(client.analytics).not_to(be_none)
        expect(client.analytics.itinerary_price_metrics).not_to(be_none)

    with it('should define all expected .get methods'):
        client = self.client
        expect(client.reference_data.urls.checkin_links.get).not_to(be_none)
        expect(client.reference_data.location('ALHR').get).not_to(be_none)
        expect(client.reference_data.locations.get).not_to(be_none)
        expect(client.reference_data.locations.airports.get).not_to(be_none)
        expect(
            client.reference_data.locations.points_of_interest.get).not_to(
            be_none)
        expect(
            client.reference_data.locations.points_of_interest.by_square.get
            ).not_to(be_none)
        expect(client.reference_data.locations.point_of_interest(
            '9CB40CB5D0').get).not_to(be_none)
        expect(client.reference_data.recommended_locations.get).not_to(be_none)

        expect(client.travel.analytics.air_traffic.traveled.get).not_to(be_none)
        expect(client.travel.analytics.air_traffic.booked.get).not_to(be_none)
        expect(
            client.travel.analytics.air_traffic.busiest_period.get).not_to(
            be_none)

        expect(client.travel.predictions.trip_purpose.get).not_to(be_none)
        expect(client.travel.predictions.flight_delay.get).not_to(be_none)

        expect(client.shopping.flight_dates.get).not_to(be_none)
        expect(client.shopping.flight_destinations.get).not_to(be_none)
        expect(client.shopping.flight_offers_search.get).not_to(be_none)

        expect(client.shopping.seatmaps.get).not_to(be_none)

        expect(client.shopping.hotel_offers.get).not_to(be_none)
        expect(client.shopping.hotel_offers_by_hotel.get).not_to(be_none)
        expect(client.shopping.hotel_offer('123').get).not_to(be_none)

        expect(client.e_reputation.hotel_sentiments.get).not_to(be_none)

        expect(client.airport.predictions.on_time.get).not_to(be_none)

        expect(client.media.files.generated_photos.get).not_to(be_none)

        expect(client.travel.trip_parser_jobs.status('123').get).not_to(be_none)
        expect(client.travel.trip_parser_jobs.result('123').get).not_to(be_none)

        expect(client.booking.flight_order('123').get).not_to(be_none)
        expect(client.booking.flight_order('123').delete).not_to(be_none)

        expect(client.safety.safety_rated_locations.by_square.get).not_to(be_none)
        expect(client.safety.safety_rated_location('Q930402719').get).not_to(
            be_none)

        expect(client.schedule.flights.get).not_to(be_none)

        expect(client.analytics.itinerary_price_metrics.get).not_to(be_none)

    with it('should define all expected .delete methods'):
        client = self.client
        expect(client.booking.flight_order('123').delete).not_to(be_none)

    with it('should define all expected .post methods'):
        client = self.client
        expect(client.travel.trip_parser_jobs.post).not_to(be_none)

    with context('testing all calls to the client'):
        with before.each:
            self.client.get = method_returning(None)
            self.client.post = method_returning(None)
            self.client.delete = method_returning(None)

        with it('.reference_data.urls.checkin_links.get'):
            self.client.reference_data.urls.checkin_links.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/reference-data/urls/checkin-links', a='b'
            ))

        with it('.reference_data.airlines.get'):
            self.client.reference_data.airlines.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/airlines', a='b'
            ))

        with it('.reference_data.location().get'):
            self.client.reference_data.location('ALHR').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/ALHR', a='b'
            ))

        with it('.reference_data.locations.get'):
            self.client.reference_data.locations.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations', a='b'
            ))

        with it('.reference_data.locations.airports.get'):
            self.client.reference_data.locations.airports.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/airports', a='b'
            ))

        with it('.reference_data.locations.points_of_interest.get'):
            self.client.reference_data.locations.points_of_interest.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/pois', a='b'
            ))

        with it('.reference_data.locations.points_of_interest.by_square.get'):
            self.client.reference_data.locations.points_of_interest.by_square.get(
                a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/pois/by-square', a='b'
            ))

        with it('.reference_data.locations.point_of_interest().get'):
            self.client.reference_data.locations.point_of_interest(
                'XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/pois/XXX', a='b'
            ))

        with it('.reference_data.recommended_locations.get'):
            self.client.reference_data.recommended_locations.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/recommended-locations', a='b'
            ))

        with it('.travel.analytics.air_traffic.traveled.get'):
            self.client.travel.analytics.air_traffic.traveled.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/analytics/air-traffic/traveled', a='b'
            ))

        with it('.travel.analytics.air_traffic.booked.get'):
            self.client.travel.analytics.air_traffic.booked.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/analytics/air-traffic/booked', a='b'
            ))

        with it('.travel.analytics.air_traffic.busiest_period.get'):
            self.client.travel.analytics.air_traffic.busiest_period.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/analytics/air-traffic/busiest-period', a='b'
            ))

        with it('.travel.predictions.trip_purpose.get'):
            self.client.travel.predictions.trip_purpose.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/predictions/trip-purpose', a='b'
            ))

        with it('.travel.predictions.flight_delay.get'):
            self.client.travel.predictions.flight_delay.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/predictions/flight-delay', a='b'
            ))

        with it('.shopping.flight_dates.get'):
            self.client.shopping.flight_dates.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/flight-dates', a='b'
            ))

        with it('.shopping.flight_destinations.get'):
            self.client.shopping.flight_destinations.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/flight-destinations', a='b'
            ))

        with it('.shopping.flight_offers_search.get'):
            self.client.shopping.flight_offers_search.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/shopping/flight-offers', a='b'
            ))

        with it('.shopping.hotel_offers.get'):
            self.client.shopping.hotel_offers.get(cityCode='MAD')
            expect(self.client.get).to(have_been_called_with(
                '/v2/shopping/hotel-offers', cityCode='MAD'
            ))

        with it('.shopping.hotel_offers_by_hotel.get'):
            self.client.shopping.hotel_offers_by_hotel.get(hotelId='XKPARC12')
            expect(self.client.get).to(have_been_called_with(
                '/v2/shopping/hotel-offers/by-hotel', hotelId='XKPARC12'
            ))

        with it('.shopping.hotel_offer().get'):
            self.client.shopping.hotel_offer('XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/shopping/hotel-offers/XXX', a='b'
            ))

        with it('.shopping.seatmaps.get'):
            self.client.shopping.seatmaps.get(**{'a': 'b'})
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/seatmaps', a='b'
            ))

        with it('.e_reputation.hotel_sentiments.get'):
            self.client.e_reputation.hotel_sentiments.get(hotelIds='XKPARC12')
            expect(self.client.get).to(have_been_called_with(
                '/v2/e-reputation/hotel-sentiments', hotelIds='XKPARC12'
            ))

        with it('.airport.predictions.on_time.get'):
            self.client.airport.predictions.on_time.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/airport/predictions/on-time', a='b'
            ))

        with it('.media.files.generated_photos.get'):
            self.client.media.files.generated_photos.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/media/files/generated-photos', a='b'
            ))

        with it('.travel.trip_parser_jobs.status().get'):
            self.client.travel.trip_parser_jobs.status('XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/travel/trip-parser-jobs/XXX', a='b'
            ))

        with it('.travel.trip_parser_jobs.result().get'):
            self.client.travel.trip_parser_jobs.result('XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/travel/trip-parser-jobs/XXX/result', a='b'
            ))

        with it('.shopping.flight_offers.prediction.post'):
            self.client.shopping.flight_offers.prediction.post({'foo': 'bar'})
            expect(self.client.post).to(have_been_called_with(
                '/v2/shopping/flight-offers/prediction', {'foo': 'bar'}
            ))

        with it('.travel.trip_parser_jobs.post'):
            self.client.travel.trip_parser_jobs.post({'foo': 'bar'})
            expect(self.client.post).to(have_been_called_with(
                '/v2/travel/trip-parser-jobs', {'foo': 'bar'}
            ))

        with it('.travel.trip_parser_jobs.post_from_base64'):
            self.client.travel.trip_parser_jobs.post(
                self.client.travel.from_base64('dGVzdA=='))
            expect(self.client.post).to(have_been_called_with(
                '/v2/travel/trip-parser-jobs',
                {'data': {'type': 'trip-parser-job', 'content': 'dGVzdA=='}}
            ))

        with it('.travel.trip_parser_jobs.post_from_file'):
            file = 'specs/namespaces/trip_parser_test.eml'
            self.client.travel.trip_parser_jobs.post(
                self.client.travel.from_file(file))
            expect(self.client.post).to(have_been_called_with(
                '/v2/travel/trip-parser-jobs',
                {'data': {'type': 'trip-parser-job', 'content': 'Qm9va2luZwo='}}
            ))

        with it('.shopping.flight_offers_search.post'):
            self.client.shopping.flight_offers_search.post({'foo': 'bar'})
            expect(self.client.post).to(have_been_called_with(
                '/v2/shopping/flight-offers', {'foo': 'bar'}
            ))

        with it('.shopping.seatmaps.post'):
            self.client.shopping.seatmaps.post({'foo': 'bar'})
            expect(self.client.post).to(have_been_called_with(
                '/v1/shopping/seatmaps', {'foo': 'bar'}
            ))

        with it('.shopping.flight_offers.pricing.post'):
            self.client.shopping.flight_offers.pricing.post(
                {'foo': 'bar'}, include='other-services')
            expect(self.client.post).to(have_been_called_with(
                '/v1/shopping/flight-offers/pricing?'+'include=other-services',
                {'data': {'type': 'flight-offers-pricing',
                          'flightOffers': [{'foo': 'bar'}]}}
            ))

        with it('.shopping.flight_offers.pricing.post_list'):
            self.client.shopping.flight_offers.pricing.post([{'foo': 'bar'}])
            expect(self.client.post).to(have_been_called_with(
                '/v1/shopping/flight-offers/pricing?',
                {'data': {'type': 'flight-offers-pricing',
                          'flightOffers': [{'foo': 'bar'}]}}
            ))

        with it('.shopping.booking.flight_orders.post'):
            self.client.booking.flight_orders.post({'foo': 'bar'}, {'bar': 'foo'})
            expect(self.client.post).to(have_been_called_with(
                '/v1/booking/flight-orders',
                {'data': {'type': 'flight-order',
                          'flightOffers': [{'foo': 'bar'}],
                          'travelers': [{'bar': 'foo'}]
                          }}
            ))

        with it('.shopping.booking.flight_orders.post_list'):
            self.client.booking.flight_orders.post(
                [{'foo': 'bar'}], [{'bar': 'foo'}])
            expect(self.client.post).to(have_been_called_with(
                '/v1/booking/flight-orders',
                {'data': {'type': 'flight-order',
                          'flightOffers': [{'foo': 'bar'}],
                          'travelers': [{'bar': 'foo'}]
                          }}
            ))

        with it('.booking.flight_order().get'):
            self.client.booking.flight_order('123').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/booking/flight-orders/123', a='b'
            ))

        with it('.booking.flight_order().delete'):
            self.client.booking.flight_order('123').delete(a='b')
            expect(self.client.delete).to(have_been_called_with(
                '/v1/booking/flight-orders/123', a='b'
            ))

        with it('.shopping.booking.hotel_bookings.post'):
            self.client.booking.hotel_bookings.post('123',
                                                    {'foo': 'bar'},
                                                    {'bar': 'foo'})
            expect(self.client.post).to(have_been_called_with(
                '/v1/booking/hotel-bookings',
                {'data': {'offerId': '123',
                          'guests': [{'foo': 'bar'}],
                          'payments': [{'bar': 'foo'}]
                          }}
            ))
        with it('.shopping.booking.hotel_bookings.post_list'):
            self.client.booking.hotel_bookings.post('123',
                                                    [{'foo': 'bar'}],
                                                    [{'bar': 'foo'}])
            expect(self.client.post).to(have_been_called_with(
                '/v1/booking/hotel-bookings',
                {'data': {'offerId': '123',
                          'guests': [{'foo': 'bar'}],
                          'payments': [{'bar': 'foo'}]
                          }}
            ))

        with it('.safety.safety_rated_locations.get'):
            self.client.safety.safety_rated_locations.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/safety/safety-rated-locations', a='b'
            ))

        with it('.safety.safety_rated_locations.by_square.get'):
            self.client.safety.safety_rated_locations.by_square.get(
                a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/safety/safety-rated-locations/by-square', a='b'
            ))

        with it('.safety.safety_rated_location().get'):
            self.client.safety.safety_rated_location('XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/safety/safety-rated-locations/XXX', a='b'
            ))

        with it('.schedule.flights().get'):
            self.client.schedule.flights.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v2/schedule/flights', a='b'
            ))
        with it('.shopping.activities.get'):
            self.client.shopping.activities.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/activities', a='b'
            ))

        with it('.shopping.activities.by_square.get'):
            self.client.shopping.activities.by_square.get(
                a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/activities/by-square', a='b'
            ))

        with it('.shopping.activity().get'):
            self.client.shopping.activity('XXX').get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/activities/XXX', a='b'
            ))

        with it('.analytics.itinerary_price_metrics().get'):
            self.client.analytics.itinerary_price_metrics.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/analytics/itinerary-price-metrics', a='b'
            ))
