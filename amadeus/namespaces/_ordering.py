from amadeus.client.decorator import Decorator
from amadeus.ordering._transfer_orders import TransferOrders
from amadeus.ordering._transfer_order import TransferOrder


class Ordering(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.transfer_orders = TransferOrders(client)

    def transfer_order(self, order_id):
        return TransferOrder(self.client, order_id)


__all__ = ['TransferOrders', 'TransferOrder']
