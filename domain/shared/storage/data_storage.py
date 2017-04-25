from abc import abstractmethod


class IDataStorage(object):
    """ Data storage interface """

    _storage = []
    _classified_storage = []

    """ Clears storage list"""
    @abstractmethod
    def clear_storage(self): raise NotImplementedError

    """ Gets all values from storage (as a tuple, which is immutable) """
    @abstractmethod
    def get_values(self): raise NotImplementedError

    """ Clear existing storage and create a new one, filled with values from the source"""
    @abstractmethod
    def load_storage(self, source): raise NotImplementedError

    """ Adds new value to existing storage """
    @abstractmethod
    def add_value(self, value): raise NotImplementedError

    """ Remove existing value from storage"""
    @abstractmethod
    def remove_value(self, value): raise NotImplementedError

    """ Groups entries by category_id ({category_id: len of values}) """
    @abstractmethod
    def calculate_categories_countability(self): raise NotImplementedError

    """ Normalizes data in data_storage """
    @abstractmethod
    def normalize_data(self): raise NotImplementedError
