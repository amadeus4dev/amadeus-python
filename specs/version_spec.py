from mamba import description, it
from expects import expect, be_none

from amadeus import version

with description('Amadeus') as self:
    with it('should have a version'):
        expect(version).not_to(be_none)
