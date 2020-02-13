Amadeus Python SDK
==================

|Module Version| |Build Status| |Maintainability| |Dependencies|
|Contact Support|

Amadeus provides a set of APIs for the travel industry. Flights, Hotels,
Locations and more.

For more details see the `Amadeus for Developers Portal
<https://developers.amadeus.com>`__ and the `class reference
<https://amadeus4dev.github.io/amadeus-python>`__ here on GitHub.

Installation
------------

This SDK requires Python 2.7+ or 3.4+. You can install it directly with pip.

.. code:: sh

    pip install amadeus

You can also add it to your `requirements.txt` file and install using:

.. code:: sh

    pip install -r requirements.txt


Getting Started
---------------

To make your first API call you will need to `register for an Amadeus Developer
Account <https://developers.amadeus.com/create-account>`__ and set up your first
application.

.. code:: py

    from amadeus import Client, ResponseError

    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET'
    )

    try:
        response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
        print(response.data)
    except ResponseError as error:
        print(error)


Initialization
--------------

The client can be initialized directly.

.. code:: py

    # Initialize using parameters
    amadeus = Client(client_id='REPLACE_BY_YOUR_API_KEY', client_secret='REPLACE_BY_YOUR_API_SECRET')

Alternatively it can be initialized without any parameters if the
environment variables ``AMADEUS_CLIENT_ID`` and
``AMADEUS_CLIENT_SECRET`` are present.

.. code:: py

    amadeus = Client()

Your credentials can be found on the `Amadeus dashboard
<https://developers.amadeus.com/my-apps/>`__. `Sign
up <https://developers.amadeus.com>`__ for an account today.

By default the environment for the SDK is the ``test`` environment. To
switch to a production (paid-for) environment please switch the hostname
as follows:

.. code:: py

    amadeus = Client(hostname='production')

Documentation
-------------

Amadeus has a large set of APIs, and our documentation is here to get you
started today. Head over to our `Reference
<https://amadeus4dev.github.io/amadeus-python/>`__
documentation for in-depth information about every SDK method, its arguments
and return types.

  -  `Initialize the SDK <https://amadeus4dev.github.io/amadeus-python/#/client>`__
  -  `Find an Airport <https://amadeus4dev.github.io/amadeus-python/#referencedata-locations>`__
  -  `Find a Flight <https://amadeus4dev.github.io/amadeus-python/#shopping-flights>`__
  -  `Get Flight Inspiration <https://amadeus4dev.github.io/amadeus-python/#shopping-flights>`__

Making API calls
----------------

This library conveniently maps every API path to a similar path.

For example, ``GET /v2/reference-data/urls/checkin-links?airlineCode=BA``
would be:

.. code:: py

    amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')

Similarly, to select a resource by ID, you can pass in the ID to the
singular path.

For example, ``GET /v2/shopping/hotel-offers/XZY`` would be:

.. code:: py

    amadeus.shopping.hotel_offer('4BA070CE929E135B3268A9F2D0C51E9D4A6CF318BA10485322FA2C7E78C7852E').get()

You can make any arbitrary API call as well directly with the ``.get``
method:

.. code:: py

    amadeus.get('/v2/reference-data/urls/checkin-links', airlineCode='BA')

Or with ``POST`` using ``.client.post`` method:

.. code:: py

    amadeus.post('/v1/shopping/flight-offers/pricing', body)

Response
--------

Every API call returns a ``Response`` object. If the API call contained
a JSON response it will parse the JSON into the ``.result`` attribute.
If this data also contains a ``data`` key, it will make that available
as the ``.data`` attribute. The raw body of the response is always
available as the ``.body`` attribute.

.. code:: py

    from amadeus import Location

    response = amadeus.reference_data.locations.get(
        keyword='LON',
        subType=Location.ANY
    )

    print(response.body) #=> The raw response, as a string
    print(response.result) #=> The body parsed as JSON, if the result was parsable
    print(response.data) #=> The list of locations, extracted from the JSON

Pagination
----------

If an API endpoint supports pagination, the other pages are available
under the ``.next``, ``.previous``, ``.last`` and ``.first`` methods.

.. code:: py

    from amadeus import Location

    response = amadeus.reference_data.locations.get(
        keyword='LON',
        subType=Location.ANY
    )

    amadeus.next(response) #=> returns a new response for the next page

If a page is not available, the method will return ``None``.

Logging & Debugging
-------------------

The SDK makes it easy to add your own logger.

.. code:: py

    import logging

    logger = logging.getLogger('your_logger')
    logger.setLevel(logging.DEBUG)

    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET',
        logger=logger
    )

Additionally, to enable more verbose logging, you can set the
appropriate level on your own logger, though the easiest way would be to
enable debugging via a parameter on initialization, or using the
``AMADEUS_LOG_LEVEL`` environment variable.

.. code:: py

    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET',
        log_level='debug'
    )

List of supported endpoints
---------------------------

.. code:: py

    # Flight Inspiration Search
    amadeus.shopping.flight_destinations.get(origin='MAD')

    # Flight Cheapest Date Search
    amadeus.shopping.flight_dates.get(origin='MAD', destination='MUC')

    # Flight Offers Search GET
    amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2020-07-01', adults=1)
    # Flight Offers Search POST
    amadeus.shopping.flight_offers_search.post(body)

    # Flight Offers Price
    flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2020-07-01', adults=1).data
    amadeus.shopping.flight_offers.pricing.post(flights[0])
    amadeus.shopping.flight_offers.pricing.post(flights[0:2], include='credit-card-fees,other-services')

    # Flight Create Orders
    amadeus.booking.flight_orders.post(flights[0], traveler)

    # Flight Order Management
    # The flight ID comes from the Flight Create Orders (in test environment it's temporary)
    flight_booking = amadeus.booking.flight_orders.post(body).data
    amadeus.booking.flight_order(flight_booking['id']).get()

    # Flight SeatMap Display GET
    amadeus.shopping.seatmaps.get(**{"flight-orderId": "orderid"})
    # Flight SeatMap Display POST
    amadeus.shopping.seatmaps.post(body)

    # Flight Low-fare Search
    amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2020-06-01')

    # Flight Choice Prediction
    body = amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2020-10-01').result
    amadeus.shopping.flight_offers.prediction.post(body)

    # Flight Checkin Links
    amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')

    # Airline Code Lookup
    amadeus.reference_data.airlines.get(airlineCodes='U2')

    # Airport and City Search (autocomplete)
    # Find all the cities and airports starting by 'LON'
    amadeus.reference_data.locations.get(keyword='LON', subType=Location.ANY)
    # Get a specific city or airport based on its id
    amadeus.reference_data.location('ALHR').get()

    # Airport Nearest Relevant Airport (for London)
    amadeus.reference_data.locations.airports.get(longitude=0.1278, latitude=51.5074)

    # Flight Most Booked Destinations
    amadeus.travel.analytics.air_traffic.booked.get(originCityCode='MAD', period='2017-08')

    # Flight Most Traveled Destinations
    amadeus.travel.analytics.air_traffic.traveled.get(originCityCode='MAD', period='2017-01')

    # Flight Busiest Travel Period
    amadeus.travel.analytics.air_traffic.busiest_period.get(cityCode='MAD', period='2017', direction='ARRIVING')
    
    # Hotel Search
    # Get list of Hotels by city code
    amadeus.shopping.hotel_offers.get(cityCode = 'LON')
    # Get list of offers for a specific hotel
    amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'BGLONBGB')
    # Confirm the availability of a specific offer
    offerId = amadeus.shopping.hotel_offer('8123DD9DE5102DADF5DA3B55C8C575F54114336EE718578753888747FE0652FC').get()

    # Hotel Booking
    # The offerId comes from the hotel_offer above
    amadeus.booking.hotel_bookings.post(offerId, guests, payments)

    # Hotel Ratings
    # What travelers think about this hotel?
    amadeus.e_reputation.hotel_sentiments.get(hotelIds = 'ADNYCCTB')

    # Point of Interest
    # What are the popular places in Barcelona (based a geo location and a radius)
    amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
    # What are the popular places in Barcelona? (based on a square)
    amadeus.reference_data.locations.points_of_interest.by_square.get(north=41.397158, west=2.160873, south=41.394582, east=2.177181)

    # Trip Purpose Prediction
    amadeus.travel.predictions.trip_purpose.get(originLocationCode='ATH', destinationLocationCode='MAD', departureDate='2020-08-01', returnDate='2020-08-12', searchDate='2020-06-11')

    # Flight Delay Prediction
    amadeus.travel.predictions.flight_delay.get(originLocationCode='NCE', destinationLocationCode='IST', departureDate='2020-08-01', \
    departureTime='18:20:00', arrivalDate='2020-08-01', arrivalTime='22:15:00', aircraftCode='321', carrierCode='TK', flightNumber='1816', duration='PT31H10M')

    # Airport On-Time Performance
    amadeus.airport.predictions.on_time.get(airportCode='JFK', date='2020-09-01')

    # AI Generated Photos
    amadeus.media.files.generated_photos.get(category='MOUNTAIN')

    # Trip Parser
    # Encode to Base64 your booking confirmation file (.html, .eml, .pdf supported)
    response = amadeus.travel.trip_parser_jobs.post(amadeus.travel.from_file(path_to_file))
    # Alternatively you can use a Base64 encoded content directly
    response = amadeus.travel.trip_parser_jobs.post(amadeus.travel.from_base64(base64))
    # Or you can call the API with the JSON directly
    response = amadeus.travel.trip_parser_jobs.post(body)
    # Get the parsing status of the process by jobId
    amadeus.travel.trip_parser_jobs.status(response.data['id']).get()
    # Get the result of the process by jobId
    amadeus.travel.trip_parser_jobs.result(response.data['id']).get()

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

Our `developer support team <https://developers.amadeus.com/support>`__ is here
to help you. You can find us on `StackOverflow <htps://stackoverflow.com/questions/tagged/amadeus>`__, and `email <mailto:developers@amadeus.com>`__.

.. |Module Version| image:: https://badge.fury.io/py/amadeus.svg
   :target: https://pypi.org/project/amadeus/
.. |Build Status| image:: http://img.shields.io/travis/amadeus4dev/amadeus-python.svg
   :target: http://travis-ci.org/amadeus4dev/amadeus-python
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/c2e19cf9628d6f4aece2/maintainability
   :target: https://codeclimate.com/github/amadeus4dev/amadeus-python/maintainability
.. |Dependencies| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/dependencies.svg?sanitize=true
   :target: https://badge.fury.io/py/amadeus
.. |Contact Support| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/support.svg?sanitize=true
   :target: http://developers.amadeus.com/support
