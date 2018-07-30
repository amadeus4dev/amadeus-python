Reference
*********

Client
======

.. autoclass:: amadeus.Client
  :members: __init__, get, post, request, previous, next, first, last

Response
========

.. autoclass:: amadeus.Response

ResponseError
=============

.. autoclass:: amadeus.ResponseError
.. autoclass:: amadeus.AuthenticationError
  :show-inheritance:
.. autoclass:: amadeus.ClientError
  :show-inheritance:
.. autoclass:: amadeus.NetworkError
  :show-inheritance:
.. autoclass:: amadeus.ServerError
  :show-inheritance:
.. autoclass:: amadeus.NotFoundError
  :show-inheritance:
.. autoclass:: amadeus.ParserError
  :show-inheritance:

Request
=======

.. autoclass:: amadeus.Request


Shopping/Flights
================

.. autoclass:: amadeus.shopping.FlightDestinations
  :members: get

.. autoclass:: amadeus.shopping.FlightDates
  :members: get

.. autoclass:: amadeus.shopping.FlightOffers
  :members: get

Shopping/Hotels
===============

.. autoclass:: amadeus.shopping.HotelOffers
  :members: get

.. autoclass:: amadeus.shopping.hotel.HotelOffers
  :members: get

.. autoclass:: amadeus.shopping.hotel.Offer
  :members: get

Travel/Analytics
================

.. autoclass:: amadeus.travel.analytics.AirTraffic
  :members: get

.. autoclass:: amadeus.travel.analytics.FareSearches
  :members: get

ReferenceData/Locations
=======================

.. autoclass:: amadeus.reference_data.Location
  :members: get

.. autoclass:: amadeus.reference_data.Locations
  :members: get

.. autoclass:: amadeus.reference_data.locations.Airports
  :members: get

.. autoclass:: amadeus.reference_data.Airlines
  :members: get

ReferenceData/Urls
==================

.. autoclass:: amadeus.reference_data.urls.CheckinLinks
  :members: get

Helper/Location
==================

.. autoclass:: amadeus.Location
