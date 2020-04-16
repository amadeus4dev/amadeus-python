import time
from amadeus import Client, ResponseError

amadeus = Client()

booking_file = 'sample.eml'

# Starts the parsing process
try:
    response = amadeus.travel.trip_parser_jobs.post(
        amadeus.travel.from_file(booking_file))
    id = response.data['id']
except ResponseError as error:
    raise error


# Retrieves the status of the process
def get_status(id):
    try:
        response = amadeus.travel.trip_parser_jobs.status(id).get()
    except ResponseError as error:
        raise error
    return response.data['status']


# Retrieves the parsing result when the process is complete
while get_status(id) != 'COMPLETED':
    time.sleep(5)
try:
    result = amadeus.travel.trip_parser_jobs.result(id).get()
except ResponseError as error:
    raise error
# print(result.data)
