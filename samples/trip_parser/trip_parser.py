import time
from amadeus import Client, ResponseError

amadeus = Client()

print('Trip Parser')
booking = './booking.eml'
try:
    response = amadeus.travel.trip_parser_jobs.post(amadeus.travel.from_file(booking))
    id = response.data['id']
    print(response.data)
except ResponseError as error:
    raise error


def get_status(id):
    response = amadeus.travel.trip_parser_jobs.status(id).get()
    print(response.data)
    return response.data['status']


while get_status(id) != 'COMPLETED':
    time.sleep(5)
result = amadeus.travel.trip_parser_jobs.result(id).get()
print(result.data)
