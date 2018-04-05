from amadeus_sdk.namespaces._reference_data import ReferenceData
from amadeus_sdk.namespaces._travel import Travel
from amadeus_sdk.namespaces._shopping import Shopping


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
        self.travel = Travel(self)
        self.shopping = Shopping(self)
