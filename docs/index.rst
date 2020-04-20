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

.. autoclass:: amadeus.shopping.FlightOffersSearch
  :members: get

.. autoclass:: amadeus.shopping.FlightOffersSearch
  :members: post

Shopping/Hotels
===============

.. autoclass:: amadeus.shopping.HotelOffers
  :members: get

.. autoclass:: amadeus.shopping.hotel.HotelOffers
  :members: get

.. autoclass:: amadeus.shopping.hotel.Offer
  :members: get

Shopping/FlightOffers
===============

.. autoclass:: amadeus.shopping.FlightOffersPrice
  :members: post

Travel/Analytics
================

.. autoclass:: amadeus.travel.analytics.AirTraffic
  :members: get

.. autoclass:: amadeus.travel.analytics.FareSearches
  :members: get

Travel/Predictions
================

.. autoclass:: amadeus.travel.predictions.TripPurpose
  :members: get

.. autoclass:: amadeus.travel.predictions.FlightDelay
  :members: get

Travel/TripParser
================

.. autoclass:: amadeus.travel.TripParser
  :members: post

.. autoclass:: amadeus.travel.trip_parser_jobs.status.TripParserStatus
  :members: get

.. autoclass:: amadeus.travel.trip_parser_jobs.result.TripParserResult
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

ReferenceData/Locations/PointsOfInterest
=======================

.. autoclass:: amadeus.reference_data.locations.PointsOfInterest
  :members: get

.. autoclass:: amadeus.reference_data.locations.points_of_interest.BySquare
  :members: get

.. autoclass:: amadeus.reference_data.locations.PointOfInterest
  :members: get

ReferenceData/Urls
==================

.. autoclass:: amadeus.reference_data.urls.CheckinLinks
  :members: get

Helper/Location
==================

.. autoclass:: amadeus.Location

Airport/Predictions
================

.. autoclass:: amadeus.airport.predictions.AirportOnTime
  :members: get

Media/Files
================

.. autoclass:: amadeus.media.files.GeneratedPhotos
  :members: get

Booking
================

.. autoclass:: amadeus.booking.FlightOrders
  :members: post

.. autoclass:: amadeus.booking.FlightOrder
  :members: get

.. autoclass:: amadeus.booking.FlightOrder
  :members: delete

.. autoclass:: amadeus.booking.HotelBookings
  :members: post