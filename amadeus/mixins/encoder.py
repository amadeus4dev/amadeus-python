import base64


# Encodes a file to Base64 format
def encode_file_to_base64(file):
    with open(file, 'rb') as opened_file:
        return base64.b64encode(opened_file.read()).decode()
