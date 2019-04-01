Changelog
=========
3.1.0 - 2019-03-25
-------------------- 
Release of the `Point of Interest API <https://developers.amadeus.com/self-service/category/210/api-doc/55>`_

The Points Of Interest API, powered by AVUXI TopPlace, is a search API that returns a list of popular places for a particular location. The location can be defined as area bound by four coordinates or as a geographical coordinate with a radius. The popularity of a place or 'point of interest' is determined by AVUXI's proprietary algorithm that considers factors such as ratings, check-ins, category scores among other factors from a host of online media sources.


3.0.0 - 2019-01-22
-------------------- 
**  Hotel Search v2 has been deployed (Hotel Search v1 is now deprecated) ** 

** General **
- Remove support of Hotel Search v1
- URLs for all three endpoints have been simplified for ease-of-use and consistency
** Find Hotels - 1st endpoint ** 
- The parameter `hotels` has been renamed to `hotelIds`
** View Hotel Rooms - 2nd endpoint ** 
- Update from `amadeus.shopping.hotel('IALONCHO').hotel_offers.get` to `amadeus.shopping.hotel_offers_by_hotel.get(hotelId: 'IALONCHO')`
- Now get all images in ‘View Hotels Rooms’ endpoint using the view parameter as `FULL_ALL_IMAGES`
** View Room Details - 3rd endpoint ** 
- Updated from `amadeus.shopping.hotel('IALONCHO').offer('XXX').get` to `amadeus.shopping.hotel_offer('XXX').get`
- Image category added under Media in the response
- Hotel distance added in the response
- Response now refers to the common HotelOffer object model

2.0.1 - 2019-01-17
-------------------- 

Fix pagination URL encoding parameters

2.0.0 - 2018-10-14
-------------------- 

`Flight Most Searched Destinations <https://developers.amadeus.com/self-service/category/203/api-doc/6>`_: Redesign of the API - Split the previous endpoint in 2 endpoints:

- 1st endpoint to find the most searched destinations
- 2nd endpoint to have more data about a dedicated origin & destination

`Flight Most Booked Destinations <https://developers.amadeus.com/self-service/category/203/api-doc/27>`_:

- Rename origin to originCityCode

`Flight Most Traveled Destinations <https://developers.amadeus.com/self-service/category/203/api-doc/7>`_:

- Rename origin in originCityCode

`Flight Check-in Links <https://developers.amadeus.com/self-service/category/203/api-doc/8>`_:

- Rename airline to airlineCode

`Airport & City Search <https://developers.amadeus.com/self-service/category/203/api-doc/10>`_:

- Remove parameter onlyMajor

`Airport Nearest Relevant <https://developers.amadeus.com/self-service/category/203/api-doc/9>`_:

- Add radius as parameter

`Airline Code Lookup <https://developers.amadeus.com/self-service/category/203/api-doc/26>`_:

- Regroup parameters *IATACode* and *ICAOCode* under the same name *airlineCodes*

1.1.0 - 2018-08-01
--------------------

Release 1.1.0

1.0.0 - 2018-04-20
--------------------

Release 1.0.0

1.0.0b8 - 2018-04-19
--------------------

Update namespace for `air_traffic/traveled` path.

1.0.0b7 - 2018-04-09
--------------------

Fix an issue where UTF8 was not properly decoded.

1.0.0b6 - 2018-04-05
--------------------

Set logging to silent by default

1.0.0b5 - 2018-04-05
--------------------

Adds easier to read error messages

1.0.0b4 - 2018-04-04
--------------------

Bug fix for install from PyPi

1.0.0b3 - 2018-04-05
--------------------

-  Renamed back to “amadeus”

1.0.0b2 - 2018-04-05
--------------------

-  Updated README for PyPi

1.0.0b1 - 2018-04-05
--------------------

-  Initial Beta Release
