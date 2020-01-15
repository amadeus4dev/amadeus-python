from amadeus import Client, ResponseError

amadeus = Client()

print('AI Generated Photos')
try:
    '''
    Generates a photo with mountain
    '''
    response = amadeus.media.files.generated_photos.get(category='MOUNTAIN')
    try:
        import urllib.request
        urllib.request.urlretrieve(response.data['attachmentUri'], 'generated_image.png')
    except ImportError:
        import urllib
        urllib.urlretrieve(response.data['attachmentUri'], 'generated_image.jpg')

    print(response.data)
except ResponseError as error:
    raise error
