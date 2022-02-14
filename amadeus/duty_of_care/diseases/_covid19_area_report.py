from amadeus.client.decorator import Decorator


class Covid19AreaReport(Decorator, object):
    def get(self, **params):
        '''
        Returns the Covid-19 restrictions on targerted area.

        .. code-block:: python

            amadeus.travel_restrictions.covid19_area_report.get(
                countryCode='US'
            )

        :param countryCode: ISO 3166 Alphas-2 code, for
            example ``"US"`` for United States of America

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/duty-of-care/diseases/covid19-area-report', **params)
