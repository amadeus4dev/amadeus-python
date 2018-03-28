from mamba import description, context, it, before
from expects import expect, be_a, raise_error, equal, be
from doublex_expects import have_been_called_with
from doublex import Spy

from amadeus import Client
from os import environ
from logging import Logger, getLogger

with description('Mixins/Validator') as self:
    with before.all:
        self.valid_params = {
            'client_id': '1234',
            'client_secret': '4546'
        }

    with context('Client.__init__'):
        with it('should create a new client with direct variables'):
            client = Client(**self.valid_params)
            expect(client).to(be_a(Client))

        with it('should create a new client with environment variables'):
            environ['AMADEUS_CLIENT_ID'] = '123'
            environ['AMADEUS_CLIENT_SECRET'] = '234'

            expect(Client()).to(be_a(Client))

            del environ['AMADEUS_CLIENT_ID']
            del environ['AMADEUS_CLIENT_SECRET']

        with context('with missing parameters'):
            with it("should refuse to create a new client without client_id"):
                del self.valid_params['client_id']
                expect(lambda: Client(**self.valid_params)).to(
                    raise_error(ValueError)
                )

            with it("should refuse to create a new client w/o client_secret"):
                del self.valid_params['client_secret']
                expect(lambda: Client(**self.valid_params)).to(
                    raise_error(ValueError)
                )

        with it('should by default have a logger'):
            amadeus = Client(**self.valid_params)
            expect(amadeus.logger).to(be_a(Logger))
            expect(amadeus.log_level).to(equal('warn'))

        with it("should allow for setting a custom logger"):
            logger = getLogger('amadeus')
            self.valid_params['logger'] = logger
            amadeus = Client(**self.valid_params)
            expect(amadeus.logger).to(be(logger))
            expect(amadeus.log_level).to(equal('warn'))

        with it("should persist a custom log level"):
            logger = getLogger('amadeus')
            logger.setLevel(10)
            self.valid_params['logger'] = logger
            amadeus = Client(**self.valid_params)
            expect(amadeus.logger).to(be(logger))
            expect(amadeus.logger.level).to(be(10))

        with it('should warn when an unrecognized option is passed in'):
            logger = Spy()
            self.valid_params['logger'] = logger
            self.valid_params['foobar'] = 'test'
            Client(**self.valid_params)
            expect(logger.warning).to(
                have_been_called_with('Unrecognized option: foobar')
            )

        with it('should default to the test host'):
            amadeus = Client(**self.valid_params)
            expect(amadeus.host).to(equal(Client.HOSTS['test']))

        with it('should allow for setting a different hostname'):
            self.valid_params['hostname'] = 'production'
            amadeus = Client(**self.valid_params)
            expect(amadeus.host).to(equal(Client.HOSTS['production']))

        with it('should allow for setting a full different host'):
            host = 'http://foo.bar.com/'
            self.valid_params['host'] = host
            amadeus = Client(**self.valid_params)
            expect(amadeus.host).to(equal(host))
