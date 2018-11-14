from amadeus.client.decorator import Decorator


class CheckinLinks(Decorator, object):
    def get(self, **params):
        '''
        Returns the checkin links for an airline, for the
        language of your choice

        .. code-block:: python

            amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')

        :param airlineCode: the IATA code for the airline, e.g. ``"BA"``
        :param language: the locale for the links, for example ``"en-GB"``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v2/reference-data/urls/checkin-links', **params)
