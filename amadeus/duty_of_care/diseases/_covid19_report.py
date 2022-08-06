from amadeus.client.decorator import Decorator


class Covid19Report(Decorator, object):
    def get(self, **params):
        '''
        Returns the Covid-19 restrictions on targeted area.

        .. code-block:: python

            amadeus.duty_of_care.diseases.covid19_report.get(
                countryCode='US'
            )

        :param countryCode: Country code following ISO 3166 Alpha-2
            standard, for example ``"US"`` for United States of America

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v2/duty-of-care/diseases/covid19-area-report', **params)
