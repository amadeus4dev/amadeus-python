import os
from mamba import description, it
from expects import expect, equal
from amadeus.mixins.encoder import encode_file_to_base64
from amadeus.travel._encoder import from_file, from_base64

with description('Mixins/Encoding'):
    with it('file should be encoded to base64'):
        file = str(os.path.dirname(os.path.abspath(__file__))) \
               + '/encoder_specs_file.eml'
        base64 = 'Ym9va2luZw=='
        expect(encode_file_to_base64(file)).to(equal(base64))

with description('Travel/From File'):
    with it('should generate the defined POST body from file'):
        file = str(os.path.dirname(os.path.abspath(__file__))) \
               + '/encoder_specs_file.eml'
        base64 = 'Ym9va2luZw=='
        body = {
            'data': {
                'type': 'trip-parser-job',
                'content': base64,
            },
        }
        expect(from_file(file)).to(equal(body))

with description('Travel/From Base64'):
    with it('should generate the defined POST body from base64'):
        base64 = 'Ym9va2luZw=='
        body = {
            'data': {
                'type': 'trip-parser-job',
                'content': base64,
            },
        }
        expect(from_base64(base64)).to(equal(body))
