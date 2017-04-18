from abc import abstractmethod


class IObservationRepository(object):
    """ Observation repository class """

    """ Find all available observations """
    def find_all(self): raise NotImplementedError

    """ Find number of different categories """
    def find_different_categories_num(self): raise NotImplementedError

    """ Find all observations in specific category """
    @abstractmethod
    def find_all_in_given_category(self, category_id): raise NotImplementedError

    """ Find observations by variables values """
    @abstractmethod
    def find_by_values(self, x, y): raise NotImplementedError


class ObservationRepository(IObservationRepository):

    def __init__(self, storage):
        self.storage = storage

    def find_all(self):
        return self.storage.get_values()

    def find_different_categories_num(self):
        return set(map(lambda o: int(o.category_id), self.storage.get_values()))

    def find_all_in_given_category(self, category_id):
        return list(filter(lambda o: int(o.category_id) == category_id, self.storage.get_values()))

    def find_category_countability(self):
        return self.storage.calculate_categories_countability()

    def find_by_values(self, x, y):
        pass
