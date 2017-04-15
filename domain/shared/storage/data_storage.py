from abc import abstractmethod


class IDataStorage(object):
    """ Data storage interface """

    _storage = []

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

