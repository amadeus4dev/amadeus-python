import os
from amadeus.mixins.encoder import encode_file_to_base64
from amadeus.travel._encoder import from_file, from_base64


def test_file_encoding():
    file = str(os.path.dirname(os.path.abspath(__file__))) \
           + '/encoder_specs_file.eml'
    base64 = 'Ym9va2luZw=='
    result = encode_file_to_base64(file)
    assert result == base64


def test_from_file():
    file = str(os.path.dirname(os.path.abspath(__file__))) \
           + '/encoder_specs_file.eml'
    base64 = 'Ym9va2luZw=='
    body = {
        'payload': base64,
    }
    result = from_file(file)
    assert result == body


def test_from_base64():
    base64 = 'Ym9va2luZw=='
    body = {
        'payload': base64,
    }
    result = from_base64(base64)
    assert result == body
