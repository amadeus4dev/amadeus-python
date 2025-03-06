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

.. autoclass:: amadeus.shopping.hotel.HotelOffersSearch
  :members: get

.. autoclass:: amadeus.shopping.hotel.HotelOfferSearch
  :members: get

Shopping/FlightOffers
===============

.. autoclass:: amadeus.shopping.flight_offers.FlightChoicePrediction
  :members: post

.. autoclass:: amadeus.shopping.flight_offers.FlightChoicePrice
  :members: post

.. autoclass:: amadeus.shopping.flight_offers.Upselling
  :members: post

Shopping/Activities
===============

.. autoclass:: amadeus.shopping.Activities
  :members: get

.. autoclass:: amadeus.shopping.activities.BySquare
  :members: get

.. autoclass:: amadeus.shopping.Activity
  :members: get

Shopping/Availability
===============

.. autoclass:: amadeus.shopping.availability.FlightAvailabilities
  :members: post

Shopping/Transfers
================

.. autoclass:: amadeus.shopping.TransferOffers
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

ReferenceData/RecommendedLocations
==================

.. autoclass:: amadeus.reference_data.RecommendedLocations
  :members: get

ReferenceData/Locations/Hotels
=======================

.. autoclass:: amadeus.reference_data.hotels.ByHotels
  :members: get

.. autoclass:: amadeus.reference_data.hotels.ByCity
  :members: get

.. autoclass:: amadeus.reference_data.hotels.ByGeocode
  :members: get

ReferenceData/Locations/Hotel
=======================

.. autoclass:: amadeus.reference_data.locations.Hotel
  :members: get

ReferenceData/Locations/Cities
=======================

.. autoclass:: amadeus.reference_data.locations.Cities
  :members: get

Helper/Location
==================

.. autoclass:: amadeus.Location

Airport/Predictions
================

.. autoclass:: amadeus.airport.predictions.AirportOnTime
  :members: get

Airport/DirectDestinations
================

.. autoclass:: amadeus.airport.DirectDestinations
  :members: get

Media/Files
================


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

.. autoclass:: amadeus.booking.HotelOrders
  :members: post


Schedule/Flights
================

.. autoclass:: amadeus.schedule.Flights
  :members: get

Analytics/ItineraryPriceMetrics
================

.. autoclass:: amadeus.analytics.ItineraryPriceMetrics
  :members: get

Airline/Destinations
================

.. autoclass:: amadeus.airline.Destinations
  :members: get

Ordering/Transfers
================

.. autoclass:: amadeus.ordering.TransferOrders
  :members: post

.. autoclass:: amadeus.ordering.transfer_orders.transfers.Cancellation
  :members: post
