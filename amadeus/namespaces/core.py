from amadeus.namespaces.reference_data import ReferenceData


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
