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

    # Flight Low-fare Search
    amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2019-08-01')

    # Flight Choice Prediction
    result = amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2019-08-01').result
    amadeus.shopping.flight_offers.prediction.post(result)

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

    # Flight Most Searched Destinations
    # Which were the most searched flight destinations from Madrid in August 2017?
    amadeus.travel.analytics.air_traffic.searched.get(originCityCode='MAD', marketCountryCode='ES', searchPeriod='2017-08')
    # How many people in Spain searched for a trip from Madrid to New-York in September 2017?
    amadeus.travel.analytics.air_traffic.searched_by_destination.get(originCityCode='MAD', destinationCityCode='NYC', marketCountryCode='ES', searchPeriod='2017-08')

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
    amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'IALONCHO')
    # Confirm the availability of a specific offer
    amadeus.shopping.hotel_offer('D5BEE9D0D08B6678C2F5FAD910DC110BCDA187D21D4FCE68ED423426D0A246BB').get()

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
   :target: ttps://badge.fury.io/py/amadeus
.. |Contact Support| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/support.svg?sanitize=true
   :target: http://developers.amadeus.com/support
