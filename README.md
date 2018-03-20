# Amadeus Python SDK

[![Module Version](https://badge.fury.io/py/amadeus.svg)](https://badge.fury.io/py/amadeus)
[![Build Status](http://img.shields.io/travis/twilio/twilio-python.svg)][travis]
[![Contact Support](https://img.shields.io/badge/contact-support-blue.svg)][support]

Amadeus provides a set of APIs for the travel industry. Flights, Hotels, Locations and more.

For more details see the [Python documentation](https://developer.amadeus.com/docs/python) on [Amadeus.com](https://developer.amadeus.com).

## Installation

This gem requires Python 2.7 or 3.6. You can install install it directly with pip.

```sh
pip install amadeus
```


__Next__: [Get Started with the Python SDK.](https://developer.amadeus.com/docs/python/get_started/initialize)

## Getting Started

To send make your first API call you will need to [register for an Amadeus Developer Account](https://developer.amadeus.com/register) and [set up your first application](https://dashboard.developer.amadeus.com/applications).

```py
import Amadeus

amadeus = amadeus.Client(
    client_id='[YOUR_CLIENT_ID]',
    client_secret='[YOUR_CLIENT_SECRET]'
)

try:
    print(amadeus.reference_data.urls.checkin_links.get(airline='1X'))
    # => {"meta"=>{"count"=>2, "links"=>{"self"=>"https://test.api.amadeus.com...
except ResponseError as error:
    print(error)
end
```

__Next__: [Learn more about checkin links](https://developer.amadeus.com/docs/python/get_started/checkin_links) with our Python SDK.

## Initialization

The client can be initialized directly.

```py
# Initialize using parameters
amadeus = amadeus.Client(client_id='...', client_secret='...')
```

Alternatively it can be initialized without any paramters if the environment variables `AMADEUS_CLIENT_ID` and `AMADEUS_CLIENT_SECRET` are present.

```py
amadeus = amadeus.Client()
```

Your credentials can be found on the [Amadeus dashboard](https://dashboard.developer.amadeus.com/client_ids). [Sign up](https://developer.amadeus.com/register) for an account today.

By default the environment for the SDK is the `test` environment. To switch to a production (paid-for) environment please switch the hostname as follows:

```py
amadeus = amadeus.Client(hostname='production')
```

__Next__: [Learn more about our initializing the Python SDK](https://developer.amadeus.com/docs/python/get_started_initialize) in our documentation.

## Documentation

Amadeus has a large set of APIs, and our documentation is here to get you started today.

* [Get Started](https://developer.amadeus.com/docs/python/get_started) documentation
  * [Initialize the SDK](https://developer.amadeus.com/docs/python/get_started/initialize)
  * [Find an Airport](https://developer.amadeus.com/docs/python/get_started/find_an_airport)
  * [Book a Flight](https://developer.amadeus.com/docs/python/get_started/book_a_flight)
  * [Get Flight Inspiration](https://developer.amadeus.com/docs/python/get_started/get_flight_inspiration)

Alternatively, head over to our [Reference](https://developer.amadeus.com/docs/python/reference) documentation for in-depth information about every SDK method, it's arguments and return types.

Additionally, this SDK has extensive documentation of itself available on [PythonDoc.info](https://workbetta.github.io/amadeus-python/).

## Making API calls

This library conveniently maps every API path to a similar path.

For example, `GET /v2/reference-data/urls/checkin-links?airline=1X` would be:

```py
amadeus.reference_data.urls.checkin_links.get(airline='1X')
```

Similarly, to select a resource by ID, you can pass in the ID to the path.

For example,  `GET /v1/shopping/hotel/123/hotel-offers` would be:

```py
amadeus.hotels(123).hotel_offers.get(...)
```

You can make any arbitrary API call as well directly with the `.get` method:

```py
amadeus.get('/v2/reference-data/urls/checkin-links', airline='1X')
```

## Response

Every API call returns a `Response` object. If the API call contained
a JSON response it will parse the JSON into the `.result` attribute. If this data
also contains a `data` key, it will make that available as the `.data`
attribute. The raw body of the response is always avaulable as the `.body` attribute.

```py
response = amadeus.reference_data.locations.get(
    keyword='LON',
    subType=Amadeus.Location.ANY
)

print(reponse.body) #=> The raw response, as a string
print(reponse.result) #=> The body parsed as JSON, if the result was parsable
print(response.data) #=> The list of locations, extracted from the JSON
```

## Pagination

If an API endpoint supports pagination, the other pages are available under the
`.next`, `.previous`, `.last` and `.first` methods.

```py
response = amadeus.reference_data.locations.get(
    keyword='LON',
    subType=Amadeus.Location.ANY
)

amadeus.next(response) #=> returns a new response for the next page
```

If a page is not available, the method will return `None`.

## Logging & Debugging

The SDK makes it easy to add your own logger.

```py
import logging

logger = logging.getLogger('your_logger')
logger.setLevel(logging.DEBUG)

amadeus = amadeus.Client(
    client_id='...',
    client_secret='...',
    logger=logger
)
```

Additionally, to enable more verbose logging, you can set the appropriate level on your own logger, though the easiest way would be to enable debugging via a parameter on initialization, or using the `AMADEUS_LOG_LEVEL` environment variable.

```py
amadeus = amadeus.Client(
    client_id='...',
    client_secret='...',
    log_level='debug'
)
```

## Development & Contributing

Want to contribute? Read our [Contributors Guide](.github/CONTRIBUTING.md) for guidance on installing and running this code in a development environment.


## License

This library is released under the [MIT License](LICENSE).

## Help

Our [developer support team](https://developer.amadeus.com/developers) is here to help you. You can find us on [Twitter](#), [StackOverflow](#), and [email](#).

[travis]: http://travis-ci.org/amdeus/amdeus-python
[support]: http://developer.amadeus.com/support
