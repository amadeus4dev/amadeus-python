from amadeus.namespaces.reference_data import ReferenceData
from amadeus.namespaces.travel import Travel
from amadeus.namespaces.shopping import Shopping


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
        self.travel = Travel(self)
        self.shopping = Shopping(self)
