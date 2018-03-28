from mamba import description, it
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
        expect(self.client.reference_data).not_to(be_none);
        expect(self.client.reference_data.urls).not_to(be_none);
        expect(self.client.reference_data.urls.checkin_links).not_to(be_none);
        expect(self.client.reference_data.location).not_to(be_none);
        expect(self.client.reference_data.locations).not_to(be_none);
        expect(self.client.reference_data.locations.airports).not_to(be_none);

        # expect(self.client.travel).not_to(be_none);
        # expect(self.client.travel.analytics).not_to(be_none);
        # expect(self.client.travel.analytics.air_traffics).not_to(be_none);
        # expect(self.client.travel.analytics.fare_searches).not_to(be_none);
        #
        # expect(self.client.shopping).not_to(be_none);
        # expect(self.client.shopping.flight_dates).not_to(be_none);
        # expect(self.client.shopping.flight_destinations).not_to(be_none);
        # expect(self.client.shopping.flight_offers).not_to(be_none);
        #
        # expect(self.client.shopping.hotel_offers).not_to(be_none);
        # expect(self.client.shopping.hotel).not_to(be_none);
        # expect(self.client.shopping.hotel(123).offer).not_to(be_none);
        # expect(self.client.shopping.hotel(123).hotel_offers).not_to(be_none);

    with it('should define all expected .get methods'):
        expect(self.client.reference_data.urls.checkin_links.get).not_to(be_none);
        expect(self.client.reference_data.location('ALHR').get).not_to(be_none);
        expect(self.client.reference_data.locations.get).not_to(be_none);
        expect(self.client.reference_data.locations.airports.get).not_to(be_none);

        # expect(self.client.travel.analytics.airTraffics.get).toBeDefined();
        # expect(self.client.travel.analytics.fareSearches.get).toBeDefined();
        #
        # expect(self.client.shopping.flightDates.get).toBeDefined();
        # expect(self.client.shopping.flightDestinations.get).toBeDefined();
        # expect(self.client.shopping.flightOffers.get).toBeDefined();
        #
        # expect(self.client.shopping.hotelOffers.get).toBeDefined();
        # expect(self.client.shopping.hotel(123).hotelOffers.get).toBeDefined();
        # expect(self.client.shopping.hotel(123).offer(234).get).toBeDefined();

    with context('testing all calls to the client'):
        with before.each:
            self.client.get = method_returning(None)

        with it('.amadeus.reference_data.urls.checkin_links.get'):
            self.client.reference_data.urls.checkin_links.get(a='b');
            expect(self.client.get).to(have_been_called_with(
                '/v2/reference-data/urls/checkin-links', a='b'
            ))

        with it('.amadeus.reference_data.location().get'):
            self.client.reference_data.location('ALHR').get(a='b');
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/ALHR', a='b'
            ))

        with it('.amadeus.reference_data.locations.get'):
            self.client.reference_data.locations.get(a='b');
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations', a='b'
            ))

        with it('.amadeus.reference_data.locations.airports.get'):
            self.client.reference_data.locations.airports.get(a='b');
            expect(self.client.get).to(have_been_called_with(
                '/v1/reference-data/locations/airports', a='b'
            ))
