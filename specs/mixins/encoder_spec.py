import os
from mamba import description, it
from expects import expect, equal
from amadeus.mixins.encoder import encode_file_to_base64
from amadeus.travel._encoder import from_file, from_base64

with description('File Encoding'):
    with it('should be encoded to base64'):
        file = str(os.path.dirname(os.path.abspath(__file__))) \
               + '/encoder_specs_file.eml'
        base64 = 'Ym9va2luZw=='
        expect(encode_file_to_base64(file)).to(equal(base64))

with description('File to POST body'):
    with it('should generate the defined POST body'):
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

with description('Base64 ti POST body'):
    with it('should generate the defined POST body'):
        base64 = 'Ym9va2luZw=='
        body = {
            'data': {
                'type': 'trip-parser-job',
                'content': base64,
            },
        }
        expect(from_base64(base64)).to(equal(body))
