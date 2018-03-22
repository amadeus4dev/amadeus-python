from mamba import description, it
from expects import expect, be_none

import amadeus

with description('Amadeus') as self:
    with it('should have a version'):
        expect(amadeus.version).not_to(be_none)
