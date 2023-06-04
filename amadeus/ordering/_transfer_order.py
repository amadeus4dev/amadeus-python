from amadeus.client.decorator import Decorator
from amadeus.ordering.transfer_orders import Transfers


class TransferOrder(Decorator, object):
    def __init__(self, client, order_id):
        Decorator.__init__(self, client)
        self.transfers = Transfers(client, order_id)
