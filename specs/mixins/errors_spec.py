from mamba import description, context, it, before
from expects import expect, equal, be_none
from doublex import Stub, Spy
from doublex_expects import have_been_called_with, have_been_called

from amadeus import NetworkError, Response, Client

with description('ResponseError') as self:
    with context('.description'):
        with it('should determine no description if no response is present'):
            error = NetworkError(None)
            expect(error.description).to(be_none)

        with it('should determine no description if no data is present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {}

            error = NetworkError(response)
            expect(error.description).to(be_none)

        with it('should be set if errors are present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {'errors': [{'detail': 'error'}]}
            error = NetworkError(response)
            expect(error.description).to(equal([{'detail': 'error'}]))

        with it('should be set if an error_description is present'):
            response = Stub(Response)
            response.parsed = True
            response.result = {'error_description': 'error'}
            error = NetworkError(response)
            expect(error.description).to(equal({'error_description': 'error'}))

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
