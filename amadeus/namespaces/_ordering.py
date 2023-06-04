from amadeus.client.decorator import Decorator
from amadeus.ordering._transfer_orders import TransferOrders


class Ordering(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.transfer_orders = TransferOrders(client)
