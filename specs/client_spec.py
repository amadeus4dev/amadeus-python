from mamba import description, it
from expects import expect, be_none, equal

from amadeus import Client, Location

with description('Client') as self:
    with it('should exist'):
        expect(Client).not_to(be_none)

    with it('should have helper locations'):
        expect(Location).not_to(be_none)
        expect(Location.ANY).to(equal('AIRPORT,CITY'))
