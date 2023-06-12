from amadeus.client.decorator import Decorator
from amadeus.ordering.transfer_orders.transfers import Cancellation


class Transfers(Decorator, object):
    def __init__(self, client, order_id):
        Decorator.__init__(self, client)
        self.cancellation = Cancellation(client, order_id)
