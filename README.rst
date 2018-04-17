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

This SDK requires Python 2.7+ or 3.3+. You can install install it
directly with pip.

.. code:: sh

    pip install amadeus==1.0.0b7

Getting Started
---------------

To make your first API call you will need to `register for an Amadeus Developer
Account <https://developers.amadeus.com/create-account>`__ and set up your first
application.

.. code:: py

    from amadeus import Client, ResponseError

    amadeus = Client(
        client_id='[YOUR_CLIENT_ID]',
        client_secret='[YOUR_CLIENT_SECRET]'
    )

    try:
        response = amadeus.reference_data.urls.checkin_links.get(airline='1X')
        print(response.data)
        # => [{'type': 'checkin-link', 'id': '1XEN-GBWeb', 'href': 'https://www....
    except ResponseError as error:
        print(error)


Initialization
--------------

The client can be initialized directly.

.. code:: py

    # Initialize using parameters
    amadeus = Client(client_id='...', client_secret='...')

Alternatively it can be initialized without any paramters if the
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

For example, ``GET /v2/reference-data/urls/checkin-links?airline=1X``
would be:

.. code:: py

    amadeus.reference_data.urls.checkin_links.get(airline='1X')

Similarly, to select a resource by ID, you can pass in the ID to the
singular path.

For example, ``GET /v1/shopping/hotels/123/hotel-offers`` would be:

.. code:: py

    amadeus.hotel(123).hotel_offers.get(...)

You can make any arbitrary API call as well directly with the ``.get``
method:

.. code:: py

    amadeus.get('/v2/reference-data/urls/checkin-links', airline='1X')

Response
--------

Every API call returns a ``Response`` object. If the API call contained
a JSON response it will parse the JSON into the ``.result`` attribute.
If this data also contains a ``data`` key, it will make that available
as the ``.data`` attribute. The raw body of the response is always
avaulable as the ``.body`` attribute.

.. code:: py

    from amadeus import Location

    response = amadeus.reference_data.locations.get(
        keyword='LON',
        subType=Location.ANY
    )

    print(reponse.body) #=> The raw response, as a string
    print(reponse.result) #=> The body parsed as JSON, if the result was parsable
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
        client_id='...',
        client_secret='...',
        logger=logger
    )

Additionally, to enable more verbose logging, you can set the
appropriate level on your own logger, though the easiest way would be to
enable debugging via a parameter on initialization, or using the
``AMADEUS_LOG_LEVEL`` environment variable.

.. code:: py

    amadeus = Client(
        client_id='...',
        client_secret='...',
        log_level='debug'
    )

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
to help you.  You can find us on `StackOverflow
<https://stackoverflow.com/questions/tagged/amadeus>`__, and `email
<mailto:developers@amadeus.com>`__.

.. |Module Version| image:: https://badge.fury.io/py/amadeus.svg?v=1
   :target: https://pypi.org/project/amadeus/
.. |Build Status| image:: http://img.shields.io/travis/amadeus4dev/amadeus-python.svg
   :target: http://travis-ci.org/amadeus4dev/amadeus-python
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/c2e19cf9628d6f4aece2/maintainability
   :target: https://codeclimate.com/github/amadeus4dev/amadeus-python/maintainability
.. |Dependencies| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/dependencies.svg?sanitize=true
   :target: ttps://badge.fury.io/py/amadeus
.. |Contact Support| image:: https://raw.githubusercontent.com/amadeus4dev/amadeus-python/master/.github/images/support.svg?sanitize=true
   :target: http://developers.amadeus.com/support
