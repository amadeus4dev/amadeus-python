from amadeus.client.decorator import Decorator


class Offer(Decorator, object):
    def __init__(self, client, hotel_id, offer_id):
        Decorator.__init__(self, client)
        self.hotel_id = hotel_id
        self.offer_id = offer_id

    def get(self, **params):
        '''
        Get room and rate details for a specific hotel offer

        .. code-block:: python

            amadeus.shopping.hotel(
                'SMPARCOL'
            ).offers('AC7D4DA2C322A73AF0824318A4965DA2805A3FC2').get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/shopping/hotels/{0}/offers/{1}'.format(
                self.hotel_id, self.offer_id
            ), **params)
