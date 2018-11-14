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

        expect(client.travel).not_to(be_none)
        expect(client.travel.analytics).not_to(be_none)
        expect(client.travel.analytics.air_traffic.traveled).not_to(be_none)
        expect(client.travel.analytics.air_traffic.searched).not_to(be_none)
        expect(client.travel.analytics.air_traffic.booked).not_to(be_none)
        expect(
            client.travel.analytics.air_traffic.searched_by_destination).not_to(
            be_none)
        expect(client.travel.analytics.air_traffic.busiest_period).not_to(be_none)

        expect(client.shopping).not_to(be_none)
        expect(client.shopping.flight_dates).not_to(be_none)
        expect(client.shopping.flight_destinations).not_to(be_none)
        expect(client.shopping.flight_offers).not_to(be_none)

        expect(client.shopping.hotel_offers).not_to(be_none)
        expect(client.shopping.hotel).not_to(be_none)
        expect(client.shopping.hotel(123).offer).not_to(be_none)
        expect(client.shopping.hotel(123).hotel_offers).not_to(be_none)

    with it('should define all expected .get methods'):
        client = self.client
        expect(client.reference_data.urls.checkin_links.get).not_to(be_none)
        expect(client.reference_data.location('ALHR').get).not_to(be_none)
        expect(client.reference_data.locations.get).not_to(be_none)
        expect(client.reference_data.locations.airports.get).not_to(be_none)

        expect(client.travel.analytics.air_traffic.traveled.get).not_to(be_none)
        expect(client.travel.analytics.air_traffic.booked.get).not_to(be_none)
        expect(client.travel.analytics.air_traffic.searched.get).not_to(be_none)
        expect(
            client.travel.analytics.air_traffic.
            searched_by_destination.get).not_to(
            be_none)
        expect(
            client.travel.analytics.air_traffic.busiest_period.get).not_to(
            be_none)

        expect(client.shopping.flight_dates.get).not_to(be_none)
        expect(client.shopping.flight_destinations.get).not_to(be_none)
        expect(client.shopping.flight_offers.get).not_to(be_none)

        expect(client.shopping.hotel_offers.get).not_to(be_none)
        expect(client.shopping.hotel(123).hotel_offers.get).not_to(be_none)
        expect(client.shopping.hotel(123).offer(234).get).not_to(be_none)

    with context('testing all calls to the client'):
        with before.each:
            self.client.get = method_returning(None)

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

        with it('.travel.analytics.air_traffic.searched.get'):
            self.client.travel.analytics.air_traffic.searched.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/travel/analytics/air-traffic/searched', a='b'
            ))

        with it('.travel.analytics.air_traffic.searched_by_destination.get'):
            self.client.travel.analytics.air_traffic.searched_by_destination.get(
                a='b')
            expect(
                self.client.get).to(
                have_been_called_with(
                    '/v1/travel/analytics/air-traffic/searched/by-destination',
                    a='b'))

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

        with it('.shopping.flight_offers.get'):
            self.client.shopping.flight_offers.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/flight-offers', a='b'
            ))

        with it('.shopping.hotel_offers.get'):
            self.client.shopping.hotel_offers.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/hotel-offers', a='b'
            ))

        with it('.shopping.hotel(123).hotel_offers.get'):
            self.client.shopping.hotel(123).hotel_offers.get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/hotels/123/hotel-offers', a='b'
            ))

        with it('.shopping.hotel(123).offer(234).get'):
            self.client.shopping.hotel(123).offer(234).get(a='b')
            expect(self.client.get).to(have_been_called_with(
                '/v1/shopping/hotels/123/offers/234', a='b'
            ))
