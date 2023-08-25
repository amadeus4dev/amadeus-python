Amadeus Python SDK
==================

|Module Version| |Build Status| |Maintainability| |Dependencies| |Discord|


Amadeus provides a rich set of APIs for the travel industry. For more details, check out the `Amadeus for Developers Portal <https://developers.amadeus.com>`__ or the `SDK class reference <https://amadeus4dev.github.io/amadeus-python>`__.

Installation
------------

This SDK requires Python 3.8+. You can install it directly with pip:

.. code:: sh

    pip install amadeus

OR, add it to your `requirements.txt` file and install using:

.. code:: sh

    pip install -r requirements.txt


Getting Started
---------------

To make your first API call, you will need to `register <https://developers.amadeus.com/register>`__ for an Amadeus Developer Account and `set up your first
application <https://developers.amadeus.com/my-apps/>`__.

.. code:: py

    from amadeus import Client, ResponseError

    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET'
    )

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='MAD', 
            destinationLocationCode='ATH', 
            departureDate='2022-11-01',
            adults=1)
        print(response.data)
    except ResponseError as error:
        print(error)

Examples
--------------------------
You can find all the endpoints in self-contained `code examples <https://github.com/amadeus4dev/amadeus-code-examples>`_.

Initialization
--------------

The client can be initialized directly.

.. code:: py

    # Initialize using parameters
    client = Client(client_id='REPLACE_BY_YOUR_API_KEY', client_secret='REPLACE_BY_YOUR_API_SECRET')

Alternatively, it can be initialized without any parameters if the environment variables ``AMADEUS_CLIENT_ID`` and ``AMADEUS_CLIENT_SECRET`` are present.

.. code:: py

    client = Client()

Your credentials can be found on the `Amadeus dashboard <https://developers.amadeus.com/my-apps/>`__.

By default, the SDK environment is set to ``test`` environment. To switch to a production (pay-as-you-go) environment, please switch the hostname as follows:

.. code:: py

    client = Client(hostname='production')

Documentation
-------------

Amadeus has a large set of APIs, and our documentation is here to get you started today. Head over to our `reference documentation <https://amadeus4dev.github.io/amadeus-python/>`__ for in-depth information about every SDK method, as well as its arguments and return types.

  -  `Initialize the SDK <https://amadeus4dev.github.io/amadeus-python/#/client>`__
  -  `Find an Airport <https://amadeus4dev.github.io/amadeus-python/#amadeus.reference_data.locations.Airports>`__
  -  `Find a Flight <https://amadeus4dev.github.io/amadeus-python/#amadeus.shopping.FlightOffersSearch>`__
  -  `Get Flight Inspiration <https://amadeus4dev.github.io/amadeus-python/#shopping-flights>`__

Making API calls
----------------

This library conveniently maps every API path to a similar path.

For example, ``GET /v2/reference-data/urls/checkin-links?airlineCode=BA`` would be:

.. code:: py

    client.reference_data.urls.checkin_links.get(airlineCode='BA')

Similarly, to select a resource by ID, you can pass in the ID to the singular path.

For example, ``GET /v2/shopping/hotel-offers/XZY`` would be:

.. code:: py

    client.shopping.hotel_offer('XYZ').get()

You can make any arbitrary API call directly with the ``.get`` method as well:

.. code:: py

    client.get('/v2/reference-data/urls/checkin-links', airlineCode='BA')

Or, with ``POST`` method:

.. code:: py

    client.post('/v1/shopping/flight-offers/pricing', body)

Response
--------

Every API call returns a ``Response`` object. If the API call contained a JSON response it will parse the JSON into the ``.result`` attribute. If this data also contains a ``data`` key, it will make that available as the ``.data`` attribute. The raw body of the response is always available as the ``.body`` attribute.

.. code:: py

    from amadeus import Location

    response = client.reference_data.locations.get(
        keyword='LON',
        subType=Location.ANY
    )

    print(response.body) #=> The raw response, as a string
    print(response.result) #=> The body parsed as JSON, if the result was parsable
    print(response.data) #=> The list of locations, extracted from the JSON

Pagination
----------

If an API endpoint supports pagination, the other pages are available under the ``.next``, ``.previous``, ``.last`` and ``.first`` methods.

.. code:: py

    from amadeus import Location

    response = client.reference_data.locations.get(
        keyword='LON',
        subType=Location.ANY
    )

    client.next(response) #=> returns a new response for the next page

If a page is not available, the method will return ``None``.

Logging & Debugging
-------------------

The SDK makes it easy to add your own logger.

.. code:: py

    import logging

    logger = logging.getLogger('your_logger')
    logger.setLevel(logging.DEBUG)

    client = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET',
        logger=logger
    )

Additionally, to enable more verbose logging, you can set the appropriate level on your own logger. The easiest way would be to enable debugging via a parameter during initialization, or using the ``AMADEUS_LOG_LEVEL`` environment variable.

.. code:: py

    client = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET',
        log_level='debug'
    )

List of supported endpoints
---------------------------

.. code:: py

    # Flight Inspiration Search
    client.shopping.flight_destinations.get(origin='MAD')

    # Flight Cheapest Date Search
    client.shopping.flight_dates.get(origin='MAD', destination='MUC')

    # Flight Offers Search GET
    client.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2022-11-01', adults=1)
    # Flight Offers Search POST
    client.shopping.flight_offers_search.post(body)

    # Flight Offers Price
    flights = client.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2022-11-01', adults=1).data
    amadeus.shopping.flight_offers.pricing.post(flights[0])
    client.shopping.flight_offers.pricing.post(flights[0:2], include='credit-card-fees,other-services')

    # Flight Create Orders
    client.booking.flight_orders.post(flights[0], traveler)

    # Flight Order Management
    # The flight ID comes from the Flight Create Orders (in test environment it's temporary)
    # Retrieve the order based on it's ID
    flight_booking = amadeus.booking.flight_orders.post(body).data
    client.booking.flight_order(flight_booking['id']).get()
    # Delete the order based on it's ID
    client.booking.flight_order(flight_booking['id']).delete()

    # Flight SeatMap Display GET
    client.shopping.seatmaps.get(**{"flight-orderId": "orderid"})
    # Flight SeatMap Display POST
    client.shopping.seatmaps.post(body)

    # Flight Availabilities POST
    client.shopping.availability.flight_availabilities.post(body)

    # Branded Fares Upsell
    client.shopping.flight_offers.upselling.post(body)

    # Flight Choice Prediction
    body = client.shopping.flight_offers_search.get(
            originLocationCode='MAD',
            destinationLocationCode='NYC',
            departureDate='2022-11-01',
            adults=1).result
    client.shopping.flight_offers.prediction.post(body)

    # Flight Checkin Links
    client.reference_data.urls.checkin_links.get(airlineCode='BA')

    # Airline Code Lookup
    client.reference_data.airlines.get(airlineCodes='U2')

    # Airport and City Search (autocomplete)
    # Find all the cities and airports starting by 'LON'
    client.reference_data.locations.get(keyword='LON', subType=Location.ANY)
    # Get a specific city or airport based on its id
    client.reference_data.location('ALHR').get()

    # City Search
    client.reference_data.locations.cities.get(keyword='PAR')

    # Airport Nearest Relevant Airport (for London)
    client.reference_data.locations.airports.get(longitude=0.1278, latitude=51.5074)

    # Flight Most Booked Destinations
    client.travel.analytics.air_traffic.booked.get(originCityCode='MAD', period='2017-08')

    # Flight Most Traveled Destinations
    client.travel.analytics.air_traffic.traveled.get(originCityCode='MAD', period='2017-01')

    # Flight Busiest Travel Period
    client.travel.analytics.air_traffic.busiest_period.get(cityCode='MAD', period='2017', direction='ARRIVING')

    # Hotel Search v3
    # Get list of available offers by hotel ids
    client.shopping.hotel_offers_search.get(hotelIds='RTPAR001', adults='2')
    # Check conditions of a specific offer
    client.shopping.hotel_offer_search('XXX').get()

    # Hotel List
    # Get list of hotels by hotel id
    client.reference_data.locations.hotels.by_hotels.get(hotelIds='ADPAR001')
    # Get list of hotels by city code
    client.reference_data.locations.hotels.by_city.get(cityCode='PAR')
    # Get list of hotels by a geocode
    client.reference_data.locations.hotels.by_geocode.get(longitude=2.160873,latitude=41.397158)

    # Hotel Name Autocomplete
    client.reference_data.locations.hotel.get(keyword='PARI', subType=[Hotel.HOTEL_GDS, Hotel.HOTEL_LEISURE])

    # Hotel Booking
    # The offerId comes from the hotel_offer above
    client.booking.hotel_bookings.post(offerId, guests, payments)

    # Hotel Ratings
    # What travelers think about this hotel?
    client.e_reputation.hotel_sentiments.get(hotelIds = 'ADNYCCTB')

    # Points of Interest
    # What are the popular places in Barcelona (based a geo location and a radius)
    client.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
    # What are the popular places in Barcelona? (based on a square)
    client.reference_data.locations.points_of_interest.by_square.get(north=41.397158, west=2.160873,
                                                                      south=41.394582, east=2.177181)
    # Returns a single Point of Interest from a given id
    client.reference_data.locations.point_of_interest('9CB40CB5D0').get()

    # Location Score
    client.location.analytics.category_rated_areas.get(latitude=41.397158, longitude=2.160873)

    # Safe Place
    # How safe is Barcelona? (based a geo location and a radius)
    client.safety.safety_rated_locations.get(latitude=41.397158, longitude=2.160873)
    # How safe is Barcelona? (based on a square)
    client.safety.safety_rated_locations.by_square.get(north=41.397158, west=2.160873,
                                                        south=41.394582, east=2.177181)
    # What is the safety information of a location based on it's Id?
    client.safety.safety_rated_location('Q930400801').get()

    # Trip Purpose Prediction
    client.travel.predictions.trip_purpose.get(originLocationCode='ATH', destinationLocationCode='MAD', departureDate='2022-11-01', returnDate='2022-11-08')

    # Flight Delay Prediction
    client.travel.predictions.flight_delay.get(originLocationCode='NCE', destinationLocationCode='IST', departureDate='2022-08-01', \
    departureTime='18:20:00', arrivalDate='2022-08-01', arrivalTime='22:15:00', aircraftCode='321', carrierCode='TK', flightNumber='1816', duration='PT31H10M')

    # Airport On-Time Performance
    client.airport.predictions.on_time.get(airportCode='JFK', date='2022-11-01')

    # Airport Routes
    client.airport.direct_destinations.get(departureAirportCode='BLR')

    # Trip Parser
    # Encode to Base64 your booking confirmation file (.html, .eml, .pdf supported)
    response = client.travel.trip_parser.post(client.travel.from_file(path_to_file))
    # Alternatively you can use a Base64 encoded content directly
    response = client.travel.trip_parser.post(client.travel.from_base64(base64))
    # Or you can call the API with the JSON directly
    response = client.travel.trip_parser.post(body)

    # Travel Recommendations
    client.reference_data.recommended_locations.get(cityCodes='PAR', travelerCountryCode='FR')

    # Retrieve status of a given flight
    client.schedule.flights.get(carrierCode='AZ', flightNumber='319', scheduledDepartureDate='2022-09-13')

    # Tours and Activities
    # What are the popular activities in Madrid (based a geo location and a radius)
    client.shopping.activities.get(latitude=40.41436995, longitude=-3.69170868)
    # What are the popular activities in Barcelona? (based on a square)
    client.shopping.activities.by_square.get(north=41.397158, west=2.160873,
                                              south=41.394582, east=2.177181)
    # Returns a single activity from a given id
    client.shopping.activity('4615').get()

    # Returns itinerary price metrics
    client.analytics.itinerary_price_metrics.get(originIataCode='MAD', destinationIataCode='CDG',
                                                departureDate='2021-03-21')

    # Travel Restrictions v2
    client.duty_of_care.diseases.covid19_report.get(countryCode='US')

    # Airline Routes
    client.airline.destinations.get(airlineCode='BA')

    # Transfer Search
    client.shopping.transfer_offers.post(body)

    # Transfer Booking
    client.ordering.transfer_orders.post(body, offerId='1000000000')

    # Transfer Management
    amadeus.ordering.transfer_order('ABC').transfers.cancellation.post(body, confirmNbr=123)

Development & Contributing
--------------------------

Want to contribute? Read our `Contributors
Guide <.github/CONTRIBUTING.md>`__ for guidance on installing and
running this code in a development environment.

License
-------

This library is released under the `MIT License <LICENSE>`__.

Help
----

You can find us on `StackOverflow <https://stackoverflow.com/questions/tagged/amadeus>`__ or join our developer community on `Discord <https://discord.gg/cVrFBqx>`__.

.. |Module Version| image:: https://badge.fury.io/py/amadeus.svg
   :target: https://pypi.org/project/amadeus/
.. |Build Status| image:: https://github.com/amadeus4dev/amadeus-python/actions/workflows/build.yml/badge.svg
   :target: https://github.com/amadeus4dev/amadeus-python/actions/workflows/build.yml
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/c2e19cf9628d6f4aece2/maintainability
   :target: https://codeclimate.com/github/amadeus4dev/amadeus-python/maintainability
.. |Dependencies| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/dependencies.svg?sanitize=true
   :target: https://badge.fury.io/py/amadeus
.. |Discord| image:: https://img.shields.io/discord/696822960023011329?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2
   :target: https://discord.gg/cVrFBqx
