import math


class Observation(object):
    """ Class representation of single observation (point in 2d) """

    def __init__(self, x, y, category_id):
        self.x = float(x)
        self.y = float(y)
        self.category_id = category_id

    def classify(self, category_id):
        """ Observation category classification can change (it depends on alghoritm configuration) """
        self.category_id = category_id

    def change_data(self, x, y):
        """ Change observation properties - return new instance (value object)"""
        return Observation(x, y, self.category_id)

    def same_as(self, other):
        """ Returns true if self and other instances points at the same observation """
        if other is None or not isinstance(other, Observation):
            raise ValueError('Other is not instance of Observation class')
        return self.x == other.x and self.y == other.y

    def scaled(self, width, height):
        """ Scales observation values to gui coordinates """
        scaled_x = 1.0 * self.x * width
        scaled_y = 1.0 * self.y * height

        scaled_x = math.fabs(scaled_x)
        scaled_y = math.fabs(scaled_y)
        return int(scaled_x), int(scaled_y)

    def rescaled(self, width, height):
        """ Re-scales gui coordinates to observation values """
        rescaled_x = 1.0 * self.x / width
        rescaled_y = 1.0 * self.y / height

        return rescaled_x, rescaled_y

    def save_format(self):
        return str(self.x) + ',' + str(self.y) + ',' + str(self.category_id)

    def __repr__(self):
        return 'Observation [' + str(self.x) + ', ' + str(self.y) + '][kategoria ' + str(self.category_id) + ']'


class ObservationFactory:
    """ Factory for creation Observation instances """

    @staticmethod
    def create_observation(x, y, category_id=None):
        """ Creates new instance of Observation based on x, y """
        if x is None or y is None:
            raise ValueError('Any observation variable cannot be None')

        if category_id is not None:
            category_id = int(category_id)

        return Observation(float(x), float(y), category_id)

    @staticmethod
    def create_observation_from_tuple(values):
        """ Creates new instance of Observation based on a tuple """
        if len(values) != 3:
            raise ValueError('Invalid observation structure')
        return ObservationFactory.create_observation(values[0], values[1], int(values[2]))