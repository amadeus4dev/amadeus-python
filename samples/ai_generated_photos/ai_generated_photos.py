from amadeus import Client, ResponseError

amadeus = Client()

print('AI Generated Photos')
try:
    '''
    Generates a photo with mountain
    '''
    response = amadeus.media.files.generated_photos.get(category='MOUNTAIN')
    print(response.data)
except ResponseError as error:
    print(error)
