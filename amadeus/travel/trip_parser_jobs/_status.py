from amadeus.client.decorator import Decorator


class TripParserStatus(Decorator, object):
    def __init__(self, client, job_id):
        Decorator.__init__(self, client)
        self.job_id = job_id

    def get(self, **params):
        '''
        Returns the parsing status and the link to the result
        in case of successful parsing.

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.status('XXX').get

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v2/travel/trip-parser-jobs/{0}'.format(self.job_id),
            **params)
