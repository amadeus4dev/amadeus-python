from mamba import description, context, it, before
from expects import expect, equal
from doublex import Stub, Spy
from doublex_expects import have_been_called_with, have_been_called

from amadeus import NetworkError, Response, Client

with description('ResponseError') as self:
    with context('str(error)'):
        with it('should be undefine if no response is present'):
            error = NetworkError(None)
            expect(str(error)).to(equal('[---]'))

        with it('should just return the code if no data is present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {}
            response.status_code = 400

            error = NetworkError(response)
            expect(str(error)).to(equal('[400]'))

        with it('should be rich if errors are present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {
                'errors': [
                    {
                        'detail': 'This field must be filled.',
                        'source': {'parameter': 'departureDate'}
                    },
                    {
                         'detail': 'This field must be filled.',
                         'source': {'parameter': 'origin'}
                    },
                    {
                         'detail': 'This field must be filled.',
                         'source': {'parameter': 'destination'}
                    }
                ]
            }
            response.status_code = 401

            error = NetworkError(response)
            expect(str(error)).to(equal(
                ('''[401]
[departureDate] This field must be filled.
[origin] This field must be filled.
[destination] This field must be filled.''')
            ))

        with it('should be rich if an error_description is present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {'error_description': 'error'}
            response.status_code = 401

            error = NetworkError(response)
            expect(str(error)).to(equal('[401]\nerror'))

    with context('.code'):
        with it('should determine the code off the class name'):
            error = NetworkError(None)
            expect(error.code).to(equal('NetworkError'))

    with context('.log'):
        with before.all:
            self.client = Stub(Client)
            self.error = NetworkError(None)
            self.error.code = 'Foo'
            self.error.description = 'Bar'

        with it('should log if the log level allows it'):
            self.client.logger = Spy()
            self.client.log_level = 'warn'
            self.error._log(self.client)
            expect(self.client.logger.warning).to(
                have_been_called_with('Amadeus %s: %s', 'Foo', "'Bar'")
            )

        with it('should not log if the log level does not allow it'):
            self.client.logger = Spy()
            self.client.log_level = 'silent'
            self.error._log(self.client)
            expect(self.client.logger.warning).not_to(have_been_called)
