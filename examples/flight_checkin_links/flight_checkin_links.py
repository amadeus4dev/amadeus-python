from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What is the URL to my online check-in?
    '''
    response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
    # print(response.data)
except ResponseError as error:
    raise error
