import os

from domain.knn.utils.alg_utils import AlghoritmUtils
from domain.shared.observation import Observation, ObservationFactory
from domain.shared.storage.data_storage import IDataStorage


class FileDataStorage(IDataStorage):
    """ Data storage based on text file """

    COMMA_SEPARATOR = ','

    def __init__(self, file):
        if not os.path.exists(file):
            raise FileNotFoundError('File ' + file + ' does not exist')
        self.storage = super()._storage
        self.load_storage(file)
        self.normalize_observations()

    def load_storage(self, source):
        with open(source) as f:
            for line in f:
                values = line.split(self.COMMA_SEPARATOR)
                try:
                    observation = ObservationFactory.create_observation_from_tuple(values)
                    self.add_value(observation)
                except ValueError:
                    self.clear_storage()
                    raise ValueError('File is corrupted')

    def get_values(self):
        return tuple(self.storage)

    def add_value(self, value):
        if not isinstance(value, Observation):
            raise ValueError('This container stores only observations')
        self.storage.append(value)

    def remove_value(self, value):
        self.storage.remove(value)

    def clear_storage(self):
        self.storage.clear()

    def calculate_categories_countability(self):
        """ Groups entries by category_id ({category_id: len of values}) """
        d = {}
        for neighbour in self.get_values():
            key = neighbour.category_id
            if key not in d:
                d[key] = 0
            d[key] += 1

        return d

    def normalize_observations(self):
        x_values = list(map(lambda o: o.x, self.storage))
        y_values = list(map(lambda o: o.y, self.storage))
        min_x = min(x_values)
        min_y = min(y_values)
        max_x = max(x_values)
        max_y = max(y_values)

        for i, observation in enumerate(self.storage):
            self.storage[i] = AlghoritmUtils.normalize_observation(observation, min_x, min_y, max_x, max_y)

        print('Data normalized')
