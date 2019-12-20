from amadeus.client.decorator import Decorator


class TripParserResult(Decorator, object):
    def __init__(self, client, job_id):
        Decorator.__init__(self, client)
        self.job_id = job_id

    def get(self, **params):
        '''
        Returns the complete result of parsing as a aggregated view of Trip

        .. code-block:: python

            amadeus.travel.trip_parser_jobs.result('XXX').get

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v2/travel/trip-parser-jobs/{0}/result'.format(self.job_id),
            **params)
