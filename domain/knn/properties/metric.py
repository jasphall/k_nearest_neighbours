from enum import Enum

import math


class Metric(Enum):
    """ Metric types """
    EUCLIDEAN = 1,
    TAXICAB = 2

    def polish_name(self):
        """ Returns polish name of metric """
        if self.name is 'EUCLIDEAN':
            return 'euklidesowa'
        elif self.name is 'TAXICAB':
            return 'miejska'
        else:
            raise ValueError('Metric type is not valid')

    @staticmethod
    def get_as_tuple():
        return Metric.EUCLIDEAN.polish_name(), Metric.TAXICAB.polish_name()

    def distance(self, p1, p2):
        """ Returns distance between two points in given metric """
        if p1.x < 0 or p1.y < 0 or p2.x < 0 or p2.y < 0:
            return ValueError('Provided points are not correct')

        if self.name is 'EUCLIDEAN':
            return self.distance_in_euclidean_metric(p1, p2)
        elif self.name is 'TAXICAB':
            return self.distance_in_taxicab_metric(p1, p2)
        else:
            raise ValueError('Metric type is not valid')

    def distance_in_euclidean_metric(self, p1, p2):
        """ Returns distance between two points in Euclidean metric """
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

    def distance_in_taxicab_metric(self, p1, p2):
        """ Returns distance between two points in Taxicab metric """
        return math.fabs(p1.y - p2.y) + math.fabs(p1.x - p2.x)
