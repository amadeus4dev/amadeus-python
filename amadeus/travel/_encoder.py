from amadeus.mixins.encoder import encode_file_to_base64


# Encodes file to Base64 and constructs POST body
def from_file(file):
    encoded_file = encode_file_to_base64(file)
    return construct_post_body(encoded_file)


# Constructs POST body from Base64
def from_base64(base64):
    return construct_post_body(base64)


# Takes a Base64 and returns a dict
def construct_post_body(base64):
    return {
        'data': {
            'type': 'trip-parser-job',
            'content': base64,
        },
    }
