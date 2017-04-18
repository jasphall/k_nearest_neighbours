from domain.knn.properties.metric import Metric
from domain.knn.properties.vote import Vote
from domain.knn.utils.alg_utils import AlghoritmUtils
from domain.shared.observation_repository import ObservationRepository
from infrastructure.utils.collection_utils import CollectionUtils


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
            if len(neighbours_category_grouped) > 1 and self.voting_tie(neighbours_category_grouped):
                ''' Tie occured '''
                return self.handle_tie_situation(observation, neighbours_category_grouped)
            else:
                max_key = self.find_dominating_category_in_neighbourhood(neighbours_category_grouped)
                return max_key
        elif self.k % 2 == 1:
            neighbours_category_grouped = self.group_neighbours_by_category(k_nearest_neighbours)
            max_key = self.find_dominating_category_in_neighbourhood(neighbours_category_grouped)
            return max_key

    def find_k_nearest_neighbours(self, observation, observations=None, k=None):
        """ Finds k nearest neighbours of given observation in specific metric """

        if observations is None:
            observations = self.observation_repository.find_all()

        if k is None:
            k = self.k

        neighbours = []

        for o in observations:
            distance = self.metric.distance(observation, o)
            if self.fits_in_minimal_values(distance, neighbours, k):
                self.update_neighbours(o, distance, neighbours, k)

        neighbours = list(map(lambda n: n['observation'], neighbours))
        return neighbours

    def fits_in_minimal_values(self, value, elements, k):
        """ Returns True, if value can be added to neighbours list """
        if len(elements) < k:
            return True

        for e in elements:
            if e['distance'] > value:
                return True

        return False

    def update_neighbours(self, observation, distance, neighbours, k):
        """ Removes most distanced neighbour in current list and inserts new observation into neighbours list """
        AlghoritmUtils.remove_most_distanced_neighbour(neighbours, k)
        neighbours.append({'observation': observation, 'distance': distance})

    def group_neighbours_by_category(self, neighbours):
        """ Groups neighbours list by category_id ({category_id: values}) """
        d = {}
        for neighbour in neighbours:
            key = neighbour.category_id
            if key not in d:
                d[key] = []
            d[key].append(neighbour)

        return d

    def find_dominating_category_in_neighbourhood(self, grouped_neighbours):
        """ Finds category, which has the biggest number of entries """
        max_key = next (iter (grouped_neighbours))
        max_value = next (iter (grouped_neighbours.values()))
        for category_id in grouped_neighbours:
            if len(grouped_neighbours[category_id]) > len(max_value):
                max_key = category_id
                max_value = grouped_neighbours[category_id]

        return max_key

    def voting_tie(self, grouped_neighbours):
        """ Returns True, if there is a tie in voting """
        first_category_len = len(next(iter(grouped_neighbours.values())))
        for category_id in grouped_neighbours:
            if len(grouped_neighbours[category_id]) != first_category_len:
                return False
        return True

    def handle_tie_situation(self, observation, grouped_neighbours):
        """ Handling tie situation """
        if self.vote == Vote.SIMPLE:
            return self.handle_tie_situation_by_simple_vote(observation, grouped_neighbours)
        else:
            return self.handle_tie_situation_by_rds_vote(observation, grouped_neighbours)

    def handle_tie_situation_by_simple_vote(self, observation, grouped_neighbours):
        """ Simple vote in case of a tie """
        category_countability = self.observation_repository.find_category_countability()
        neighbours_countability = {}

        for c_id in grouped_neighbours:
            neighbours_countability[c_id] = category_countability[c_id]

        ''' Looking for a categories that has minimal number of entries in learning set '''
        min_categories_ids = []
        min_value = None
        for category_id in neighbours_countability:
            if len(min_categories_ids) == 0:
                min_categories_ids.append(category_id)
                min_value = neighbours_countability[category_id]
            elif neighbours_countability[category_id] == min_value:
                min_categories_ids.append(category_id)
            elif neighbours_countability[category_id] < min_value:
                min_categories_ids.clear()
                min_categories_ids.append(category_id)
                min_value = neighbours_countability[category_id]

        if len(min_categories_ids) == 1:
            ''' Exists one category in dict with the smallest power '''
            return min_categories_ids[0]
        else:
            ''' There is more than one category with same (minimal) power '''
            observations = CollectionUtils.unwrap_elements(
                list(map(lambda o: grouped_neighbours[o], grouped_neighbours)))

            ''' In this case we try again to find nearest neighbour from the list of k nearest neighbours '''
            nearest = self.find_k_nearest_neighbours(observation, observations, 1)[0]
            return nearest.category_id

    def handle_tie_situation_by_rds_vote(self, observation, grouped_neighbours):
        """ Reverse distance square vote method in case of a tie """
        neighbours = CollectionUtils.unwrap_elements(
            list(map(lambda o: grouped_neighbours[o], grouped_neighbours)))

        distances = {}

        for n in neighbours:
            distance = self.metric.distance(observation, n)
            rds = 1.0 * (1/distance**2)
            distances[n] = rds

        max_rds_categories = []
        max_rds_value = None
        for neighbour in distances:
            if len(max_rds_categories) == 0:
                max_rds_categories.append(neighbour)
                max_rds_value = distances[neighbour]
            elif distances[neighbour] == max_rds_value:
                max_rds_categories.append(neighbour)
            elif distances[neighbour] > max_rds_value:
                max_rds_categories.clear()
                max_rds_categories.append(neighbour)
                max_rds_value = distances[neighbour]

        return max_rds_categories[0]





















