from amadeus.namespaces._reference_data import ReferenceData
from amadeus.namespaces._travel import Travel
from amadeus.namespaces._shopping import Shopping


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
        self.travel = Travel(self)
        self.shopping = Shopping(self)
