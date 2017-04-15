from enum import Enum


class Metric(Enum):
    """ Metric types """
    EUCLIDEAN = 1,
    TAXICAB = 2

    def polish_name(self):
        if self.name is 'EUCLIDEAN':
            return 'euklidesowa'
        elif self.name is 'TAXICAB':
            return 'miejska'
        else:
            raise ValueError('Metric type is not valid')

    @staticmethod
    def get_as_tuple():
        return Metric.EUCLIDEAN.polish_name(), Metric.TAXICAB.polish_name()
