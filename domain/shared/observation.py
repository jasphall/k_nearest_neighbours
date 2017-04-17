class Observation(object):
    """ Class representation of single observation (point in 2d) """

    def __init__(self, x, y, category_id):
        self.x = int(x)
        self.y = int(y)
        self.category_id = category_id

    def classify(self, category_id):
        """ Observation category classification can change (it depends on alghoritm configuration) """
        self.category_id = category_id

    def change_data(self, x, y):
        """ Change observation properties - return new instance (value object)"""
        return Observation(x, y, self.category_id)

    def same_as(self, other):
        if other is None or not isinstance(other, Observation):
            raise ValueError('Other is not instance of Observation class')
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'Observation [' + str(self.x) + ', ' + str(self.y) + '][kategoria ' + str(self.category_id) + ']'


class ObservationFactory:
    """ Factory for creation Observation instances """

    @staticmethod
    def create_observation(x, y, category_id=None):
        if x is None or y is None:
            raise ValueError('Any observation variable cannot be None')

        if category_id is not None:
            category_id = int(category_id)

        return Observation(int(x), int(y), category_id)

    @staticmethod
    def create_observation_from_tuple(values):
        if len(values) != 3:
            raise ValueError('Invalid observation structure')
        return ObservationFactory.create_observation(values[0], values[1], int(values[2]))