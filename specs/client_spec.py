from mamba import description, context, it
from expects import expect, be_none

from amadeus import Client

with description('Client') as self:
    with it('should exist'):
        expect(Client).not_to(be_none)
