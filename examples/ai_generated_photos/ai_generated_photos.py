from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Generates a photo with mountain
    '''
    response = amadeus.media.files.generated_photos.get(category='MOUSNTAIN')
    try:
        import urllib.request
        urllib.request.urlretrieve(response.data['attachmentUri'], 'generated_image.png')
    except ImportError:
        import urllib
        urllib.urlretrieve(response.data['attachmentUri'], 'generated_image.jpg')
except ResponseError as error:
    print(error)
    raise error
