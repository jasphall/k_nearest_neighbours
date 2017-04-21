from enum import Enum


class Vote(Enum):
    """ Vote types """
    SIMPLE = 1,
    REVERSE_DISTANCE_SQUARE = 2

    def polish_name(self):
        """ Returns polish name of vote type """
        if self.name is 'SIMPLE':
            return 'proste'
        elif self.name is 'REVERSE_DISTANCE_SQUARE':
            return 'ważone odwrotnością kwadratu odległości'
        else:
            raise ValueError('Vote type is not valid')

    @staticmethod
    def get_as_tuple():
        return Vote.SIMPLE.polish_name(), Vote.REVERSE_DISTANCE_SQUARE.polish_name()