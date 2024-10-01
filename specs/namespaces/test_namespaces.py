import pytest
from mock import MagicMock
from amadeus import Client


@pytest.fixture
def client():
    return Client(client_id='123', client_secret='234')


def test_expected_paths(client):
    assert client.reference_data is not None
    assert client.reference_data.urls is not None
    assert client.reference_data.urls.checkin_links is not None
    assert client.reference_data.location is not None
    assert client.reference_data.locations is not None
    assert client.reference_data.locations.airports is not None
    assert client.reference_data.locations.points_of_interest is not None
    assert client.reference_data.locations.points_of_interest.by_square \
        is not None
    assert client.reference_data.locations.hotels is not None
    assert client.reference_data.locations.hotels.by_hotels is not None
    assert client.reference_data.locations.hotels.by_city is not None
    assert client.reference_data.locations.hotels.by_geocode is not None
    assert client.reference_data.locations.hotel is not None
    assert client.reference_data.locations.cities is not None
    assert client.travel is not None
    assert client.travel.analytics is not None
    assert client.travel.analytics.air_traffic.traveled is not None
    assert client.travel.analytics.air_traffic.booked is not None
    assert client.travel.analytics.air_traffic.busiest_period is not None
    assert client.travel.predictions is not None
    assert client.travel.predictions.trip_purpose is not None
    assert client.travel.predictions.flight_delay is not None
    assert client.shopping is not None
    assert client.shopping.flight_dates is not None
    assert client.shopping.flight_destinations is not None
    assert client.shopping.flight_offers is not None
    assert client.shopping.flight_offers_search is not None
    assert client.shopping.flight_offers.pricing is not None
    assert client.shopping.flight_offers.upselling is not None
    assert client.shopping.seatmaps is not None
    assert client.shopping.hotel_offers_search is not None
    assert client.shopping.hotel_offer_search is not None
    assert client.shopping.activities is not None
    assert client.shopping.availability is not None
    assert client.shopping.availability.flight_availabilities is not None
    assert client.e_reputation.hotel_sentiments is not None
    assert client.airport is not None
    assert client.airport.predictions is not None
    assert client.airport.predictions.on_time is not None
    assert client.airport.direct_destinations is not None
    assert client.booking.flight_orders is not None
    assert client.booking.flight_order is not None
    assert client.booking.hotel_orders is not None
    assert client.schedule is not None
    assert client.schedule.flights is not None
    assert client.analytics is not None
    assert client.analytics.itinerary_price_metrics is not None
    assert client.location is not None
    assert client.location.analytics.category_rated_areas is not None
    assert client.airline.destinations is not None
    assert client.shopping.transfer_offers is not None
    assert client.ordering.transfer_orders is not None
    assert client.ordering.transfer_order is not None


def test_expected_get_methods(client):
    assert client.reference_data.urls.checkin_links.get is not None
    assert client.reference_data.location('ALHR').get is not None
    assert client.reference_data.locations.get is not None
    assert client.reference_data.locations.airports.get is not None
    assert client.reference_data.locations.points_of_interest.get is not None
    assert client.reference_data.locations.points_of_interest.by_square.get \
        is not None
    assert client.reference_data.locations.point_of_interest('9CB40CB5D0').get \
        is not None
    assert client.reference_data.recommended_locations.get is not None
    assert client.reference_data.locations.hotels.by_city.get is not None
    assert client.reference_data.locations.hotels.by_hotels.get is not None
    assert client.reference_data.locations.hotels.by_geocode.get is not None
    assert client.reference_data.locations.hotel.get is not None
    assert client.travel.analytics.air_traffic.traveled.get is not None
    assert client.travel.analytics.air_traffic.booked.get is not None
    assert client.travel.analytics.air_traffic.busiest_period.get is not None
    assert client.travel.predictions.trip_purpose.get is not None
    assert client.travel.predictions.flight_delay.get is not None
    assert client.shopping.flight_dates.get is not None
    assert client.shopping.flight_destinations.get is not None
    assert client.shopping.flight_offers_search.get is not None
    assert client.shopping.seatmaps.get is not None
    assert client.shopping.hotel_offers_search.get is not None
    assert client.shopping.hotel_offer_search('123').get is not None
    assert client.e_reputation.hotel_sentiments.get is not None
    assert client.airport.predictions.on_time.get is not None
    assert client.airport.direct_destinations.get is not None
    assert client.booking.flight_order('123').get is not None
    assert client.booking.flight_order('123').delete is not None
    assert client.schedule.flights.get is not None
    assert client.analytics.itinerary_price_metrics.get is not None
    assert client.location.analytics.category_rated_areas.get is not None
    assert client.airline.destinations.get is not None


def test_expected_delete_methods(client):
    assert client.booking.flight_order('123').delete is not None
    assert client.reference_data.location('ALHR').get is not None
    assert client.reference_data.locations.get is not None


@pytest.fixture
def client_setup():
    client = Client(client_id='123', client_secret='234')
    client.get = MagicMock(return_value=None)
    client.post = MagicMock(return_value=None)
    client.delete = MagicMock(return_value=None)
    yield client


def test_reference_data_urls_checkin_links_get(client_setup):
    client_setup.reference_data.urls.checkin_links.get(a='b')
    client_setup.get.assert_called_with(
        '/v2/reference-data/urls/checkin-links',
        a='b'
    )


def test_reference_data_airlines_get(client_setup):
    client_setup.reference_data.airlines.get(a='b')
    client_setup.get.assert_called_with('/v1/reference-data/airlines', a='b')


def test_reference_data_location_get(client_setup):
    client_setup.reference_data.location('ALHR').get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/ALHR', a='b'
    )


def test_reference_data_locations_get(client_setup):
    client_setup.reference_data.locations.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations', a='b'
    )


def test_reference_data_locations_airports_get(client_setup):
    client_setup.reference_data.locations.airports.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/airports', a='b'
    )


def test_reference_data_locations_points_of_interest_get(client_setup):
    client_setup.reference_data.locations.points_of_interest.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/pois', a='b'
    )


def test_reference_data_locations_points_of_interest_by_square_get(client_setup):
    client_setup.reference_data.locations.points_of_interest.by_square.get(
        a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/pois/by-square', a='b'
    )


def test_reference_data_locations_point_of_interest_get(client_setup):
    client_setup.reference_data.locations.point_of_interest(
        'XXX').get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/pois/XXX', a='b'
    )


def test_location_analytics_category_rated_areas_get(client_setup):
    client_setup.location.analytics.category_rated_areas.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/location/analytics/category-rated-areas', a='b'
    )


def test_reference_data_recommended_locations_get(client_setup):
    client_setup.reference_data.recommended_locations.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/recommended-locations', a='b'
    )


def test_travel_analytics_air_traffic_traveled_get(client_setup):
    client_setup.travel.analytics.air_traffic.traveled.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/travel/analytics/air-traffic/traveled', a='b'
    )


def test_travel_analytics_air_traffic_booked_get(client_setup):
    client_setup.travel.analytics.air_traffic.booked.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/travel/analytics/air-traffic/booked', a='b'
    )


def test_travel_analytics_air_traffic_busiest_period_get(client_setup):
    client_setup.travel.analytics.air_traffic.busiest_period.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/travel/analytics/air-traffic/busiest-period', a='b'
    )


def test_travel_predictions_trip_purpose_get(client_setup):
    client_setup.travel.predictions.trip_purpose.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/travel/predictions/trip-purpose', a='b'
    )


def test_travel_predictions_flight_delay_get(client_setup):
    client_setup.travel.predictions.flight_delay.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/travel/predictions/flight-delay', a='b'
    )


def test_shopping_flight_dates_get(client_setup):
    client_setup.shopping.flight_dates.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/shopping/flight-dates', a='b'
    )


def test_shopping_flight_destinations_get(client_setup):
    client_setup.shopping.flight_destinations.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/shopping/flight-destinations', a='b'
    )


def test_shopping_flight_offers_search_get(client_setup):
    client_setup.shopping.flight_offers_search.get(a='b')
    client_setup.get.assert_called_with(
        '/v2/shopping/flight-offers', a='b'
    )


def test_shopping_hotel_offers_search_get(client_setup):
    client_setup.shopping.hotel_offers_search.get(
        hotelIds='RTPAR001', adults=2)
    client_setup.get.assert_called_with(
        '/v3/shopping/hotel-offers', hotelIds='RTPAR001',
        adults=2
    )


def test_shopping_hotel_offer_search_get(client_setup):
    client_setup.shopping.hotel_offer_search('XXX').get(a='b')
    client_setup.get.assert_called_with(
        '/v3/shopping/hotel-offers/XXX', a='b'
    )


def test_shopping_seatmaps_get(client_setup):
    client_setup.shopping.seatmaps.get(**{'a': 'b'})
    client_setup.get.assert_called_with(
        '/v1/shopping/seatmaps', a='b'
    )


def test_e_reputation_hotel_sentiments_get(client_setup):
    client_setup.e_reputation.hotel_sentiments.get(hotelIds='XKPARC12')
    client_setup.get.assert_called_with(
        '/v2/e-reputation/hotel-sentiments', hotelIds='XKPARC12'
    )


def test_airport_predictions_on_time_get(client_setup):
    client_setup.airport.predictions.on_time.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/airport/predictions/on-time', a='b'
    )


def test_airport_direct_destinations_get(client_setup):
    client_setup.airport.direct_destinations.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/airport/direct-destinations', a='b'
    )


def test_shopping_flight_offers_prediction_post(client_setup):
    client_setup.shopping.flight_offers.prediction.post({'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v2/shopping/flight-offers/prediction', {'foo': 'bar'}
    )


def test_shopping_flight_offers_search_post(client_setup):
    client_setup.shopping.flight_offers_search.post({'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v2/shopping/flight-offers', {'foo': 'bar'}
    )


def test_shopping_seatmaps_post(client_setup):
    client_setup.shopping.seatmaps.post({'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v1/shopping/seatmaps', {'foo': 'bar'}
    )


def test_shopping_flight_offers_pricing_post(client_setup):
    client_setup.shopping.flight_offers.pricing.post(
        {'foo': 'bar'}, include='other-services')
    client_setup.post.assert_called_with(
        '/v1/shopping/flight-offers/pricing?'+'include=other-services',
        {'data': {'type': 'flight-offers-pricing',
                  'flightOffers': [{'foo': 'bar'}]}}
    )


def test_shopping_flight_offers_pricing_post_list(client_setup):
    client_setup.shopping.flight_offers.pricing.post([{'foo': 'bar'}])
    client_setup.post.assert_called_with(
        '/v1/shopping/flight-offers/pricing?',
        {'data': {'type': 'flight-offers-pricing',
                  'flightOffers': [{'foo': 'bar'}]}}
    )


def test_shopping_booking_flight_orders_post(client_setup):
    client_setup.booking.flight_orders.post({'foo': 'bar'}, {'bar': 'foo'})
    client_setup.post.assert_called_with(
        '/v1/booking/flight-orders',
        {'data': {'type': 'flight-order',
                  'flightOffers': [{'foo': 'bar'}],
                  'travelers': [{'bar': 'foo'}]
                  }}
    )


def test_shopping_booking_flight_orders_post_list(client_setup):
    client_setup.booking.flight_orders.post(
        [{'foo': 'bar'}], [{'bar': 'foo'}])
    client_setup.post.assert_called_with(
        '/v1/booking/flight-orders',
        {'data': {'type': 'flight-order',
                  'flightOffers': [{'foo': 'bar'}],
                  'travelers': [{'bar': 'foo'}]
                  }}
    )


def test_shopping_availability_flight_availabilities_post(client_setup):
    client_setup.shopping.availability.flight_availabilities.post(
        {'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v1/shopping/availability/flight-availabilities', {'foo': 'bar'}
    )


def test_shopping_flight_offers_upselling_post(client_setup):
    client_setup.shopping.flight_offers.upselling.post(
        {'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v1/shopping/flight-offers/upselling', {'foo': 'bar'}
    )


def test_booking_flight_order_get(client_setup):
    client_setup.booking.flight_order('123').get(a='b')
    client_setup.get.assert_called_with(
        '/v1/booking/flight-orders/123', a='b'
    )


def test_booking_flight_order_delete(client_setup):
    client_setup.booking.flight_order('123').delete(a='b')
    client_setup.delete.assert_called_with(
        '/v1/booking/flight-orders/123', a='b'
    )


def test_shopping_booking_hotel_bookings_post(client_setup):
    client_setup.booking.hotel_bookings.post('123',
                                             {'foo': 'bar'},
                                             {'bar': 'foo'})
    client_setup.post.assert_called_with(
        '/v1/booking/hotel-bookings',
        {'data': {'offerId': '123',
                  'guests': [{'foo': 'bar'}],
                  'payments': [{'bar': 'foo'}]
                  }}
    )


def test_shopping_booking_hotel_bookings_post_list(client_setup):
    client_setup.booking.hotel_bookings.post('123',
                                             [{'foo': 'bar'}],
                                             [{'bar': 'foo'}])
    client_setup.post.assert_called_with(
        '/v1/booking/hotel-bookings',
        {'data': {'offerId': '123',
                  'guests': [{'foo': 'bar'}],
                  'payments': [{'bar': 'foo'}]
                  }}
    )


def test_booking_hotel_orders_post(client_setup):
    client_setup.booking.hotel_orders.post({'foo': 'bar'},
                                           {'bar': 'foo'})
    client_setup.post.assert_called_with(
        '/v2/booking/hotel-orders',
        {'data': {'type': 'hotel-order',
                  'guests': [{'foo': 'bar'}],
                  'travelAgent': {'bar': 'foo'},
                  'roomAssociations': [],
                  'payment': {},
                  'arrivalInformation': {}}}
    )


def test_booking_hotel_orders_post_list(client_setup):
    client_setup.booking.hotel_orders.post([{'foo': 'bar'}],
                                           {'bar': 'foo'},
                                           [{'a': 'b'}],)
    client_setup.post.assert_called_with(
        '/v2/booking/hotel-orders',
        {'data': {'type': 'hotel-order',
                  'guests': [{'foo': 'bar'}],
                  'travelAgent': {'bar': 'foo'},
                  'roomAssociations': [{'a': 'b'}],
                  'payment': {},
                  'arrivalInformation': {}}}
    )


def test_schedule_flights_get(client_setup):
    client_setup.schedule.flights.get(a='b')
    client_setup.get.assert_called_with(
        '/v2/schedule/flights', a='b'
    )


def test_shopping_activities_get(client_setup):
    client_setup.shopping.activities.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/shopping/activities', a='b'
    )


def test_shopping_activities_by_square_get(client_setup):
    client_setup.shopping.activities.by_square.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/shopping/activities/by-square', a='b'
    )


def test_shopping_activity_get(client_setup):
    client_setup.shopping.activity('XXX').get(a='b')
    client_setup.get.assert_called_with(
        '/v1/shopping/activities/XXX', a='b'
    )


def test_analytics_itinerary_price_metrics_get(client_setup):
    client_setup.analytics.itinerary_price_metrics.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/analytics/itinerary-price-metrics', a='b'
    )


def test_reference_data_locations_hotels_by_hotels_get(client_setup):
    client_setup.reference_data.locations.hotels.by_hotels.get(a='b',
                                                               c=['d', 'e'])
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/hotels/by-hotels', a='b', c='d,e'
    )


def test_reference_data_locations_hotels_by_city_get(client_setup):
    client_setup.reference_data.locations.hotels.by_city.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/hotels/by-city', a='b'
    )


def test_reference_data_locations_hotels_by_geocode_get(client_setup):
    client_setup.reference_data.locations.hotels.by_geocode.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/hotels/by-geocode', a='b'
    )


def test_reference_data_locations_hotel_get(client_setup):
    client_setup.reference_data.locations.hotel.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/hotel', a='b'
    )


def test_reference_data_locations_cities_get(client_setup):
    client_setup.reference_data.locations.cities.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/reference-data/locations/cities', a='b'
    )


def test_airline_destinations_get(client_setup):
    client_setup.airline.destinations.get(a='b')
    client_setup.get.assert_called_with(
        '/v1/airline/destinations', a='b'
    )


def test_shopping_transfer_offers_post(client_setup):
    client_setup.shopping.transfer_offers.post({'foo': 'bar'})
    client_setup.post.assert_called_with(
        '/v1/shopping/transfer-offers', {'foo': 'bar'}
    )


def test_ordering_transfer_orders_post(client_setup):
    client_setup.ordering.transfer_orders.post(
        {'foo': 'bar'}, offerId='1')
    client_setup.post.assert_called_with(
        '/v1/ordering/transfer-orders?'+'offerId=1', {'foo': 'bar'}
    )


def test_ordering_transfer_order_transfers_cancellation_post(client_setup):
    client_setup.ordering.transfer_order('XXX').transfers.cancellation.post(
        {'foo': 'bar'}, confirmNbr=123)
    client_setup.post.assert_called_with(
        '/v1/ordering/transfer-orders/XXX/transfers/cancellation?confirmNbr=123',
        {'foo': 'bar'}
    )
