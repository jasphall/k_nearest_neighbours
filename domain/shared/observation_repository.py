from abc import abstractmethod


class IObservationRepository(object):
    """ Observation repository class """

    """ Find all observations in specific category """
    @abstractmethod
    def find_all_by_category_id(self, category_id): raise NotImplementedError

    """ Find observations by variables values """
    @abstractmethod
    def find_by_values(self, x, y): raise NotImplementedError


class ObservationRepository(IObservationRepository):

    def find_all_by_category_id(self, category_id):
        pass

    def find_by_values(self, x, y):
        pass
