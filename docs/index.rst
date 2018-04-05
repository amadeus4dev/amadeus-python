Reference
*********

Client
======

.. autoclass:: amadeus_sdk.Client
  :members: __init__, get, post, request, previous, next, first, last

Response
========

.. autoclass:: amadeus_sdk.Response

ResponseError
=============

.. autoclass:: amadeus_sdk.ResponseError
.. autoclass:: amadeus_sdk.AuthenticationError
  :show-inheritance:
.. autoclass:: amadeus_sdk.ClientError
  :show-inheritance:
.. autoclass:: amadeus_sdk.NetworkError
  :show-inheritance:
.. autoclass:: amadeus_sdk.ServerError
  :show-inheritance:
.. autoclass:: amadeus_sdk.NotFoundError
  :show-inheritance:
.. autoclass:: amadeus_sdk.ParserError
  :show-inheritance:

Request
=======

.. autoclass:: amadeus_sdk.Request


Shopping/Flights
================

.. autoclass:: amadeus_sdk.shopping.FlightDestinations
  :members: get

.. autoclass:: amadeus_sdk.shopping.FlightDates
  :members: get

.. autoclass:: amadeus_sdk.shopping.FlightOffers
  :members: get

Shopping/Hotels
===============

.. autoclass:: amadeus_sdk.shopping.HotelOffers
  :members: get

.. autoclass:: amadeus_sdk.shopping.hotel.HotelOffers
  :members: get

.. autoclass:: amadeus_sdk.shopping.hotel.Offer
  :members: get

Travel/Analytics
================

.. autoclass:: amadeus_sdk.travel.analytics.AirTraffics
  :members: get

.. autoclass:: amadeus_sdk.travel.analytics.FareSearches
  :members: get

ReferenceData/Locations
=======================

.. autoclass:: amadeus_sdk.reference_data.Location
  :members: get

.. autoclass:: amadeus_sdk.reference_data.Locations
  :members: get

.. autoclass:: amadeus_sdk.reference_data.locations.Airports
  :members: get

ReferenceData/Urls
==================

.. autoclass:: amadeus_sdk.reference_data.urls.CheckinLinks
  :members: get

Helper/Location
==================

.. autoclass:: amadeus_sdk.Location
