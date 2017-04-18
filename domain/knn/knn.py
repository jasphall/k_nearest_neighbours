from domain.knn.properties.metric import Metric
from domain.knn.properties.vote import Vote
from domain.knn.utils.alg_utils import AlghoritmUtils
from domain.shared.observation_repository import ObservationRepository


class KNNAlghoritm:

    def __init__(self, data_storage):
        self.observation_repository = ObservationRepository(data_storage)
        self.k = 1
        self.metric = Metric.EUCLIDEAN
        self.vote = Vote.SIMPLE

    def setup_k(self, k):
        self.k = k

    def setup_metric(self, metric):
        self.metric = metric

    def setup_vote(self, vote):
        self.vote = vote

    def classify(self, observation):
        k_nearest_neighbours = self.find_k_nearest_neighbours(observation)

        if len(k_nearest_neighbours) != self.k:
            raise ArithmeticError('Method find_k_nearest_neighbours does not work good')

        if self.k == 1:
            return k_nearest_neighbours[0].category_id
        elif self.k % 2 == 0:
            neighbours_category_grouped = self.group_neighbours_by_category(k_nearest_neighbours)
            pass
        elif self.k % 2 == 1:
            neighbours_category_grouped = self.group_neighbours_by_category(k_nearest_neighbours)
            max_key = self.find_dominating_category_in_neighbourhood(neighbours_category_grouped)
            return max_key

    def find_k_nearest_neighbours(self, observation):
        """ Finds k nearest neighbours of given observation in specific metric """
        observations = self.observation_repository.find_all()
        neighbours = []

        for o in observations:
            distance = self.metric.distance(observation, o)
            if self.fits_in_minimal_values(distance, neighbours):
                self.update_neighbours(o, distance, neighbours)

        neighbours = list(map(lambda n: n['observation'], neighbours))
        return neighbours

    def fits_in_minimal_values(self, value, elements):
        """ Returns True, if value can be added to neighbours list """
        if len(elements) < self.k:
            return True

        for e in elements:
            if e['distance'] > value:
                return True

        return False

    def update_neighbours(self, observation, distance, neighbours):
        """ Removes most distanced neighbour in current list and inserts new observation into neighbours list """
        AlghoritmUtils.remove_most_distanced_neighbour(neighbours, self.k)
        neighbours.append({'observation': observation, 'distance': distance})

    def group_neighbours_by_category(self, neighbours):
        d = {}
        for neighbour in neighbours:
            key = neighbour.category_id
            if key not in d:
                d[key] = []
            d[key].append(neighbour)

        return d

    def find_dominating_category_in_neighbourhood(self, grouped_neighbours):
        min_key = next (iter (grouped_neighbours))
        min_value = next (iter (grouped_neighbours.values()))
        for category_id in grouped_neighbours:
            if len(grouped_neighbours[category_id]) > len(min_value):
                min_key = category_id
                min_value = grouped_neighbours[category_id]

        return min_key