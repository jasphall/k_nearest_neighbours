from PyQt5.QtCore import pyqtSlot, QObject

from domain.knn.knn import KNNAlghoritm
from domain.knn.properties.metric import Metric
from domain.knn.properties.vote import Vote
from domain.shared.observation import ObservationFactory
from infrastructure.events.events import Events


class EventsHandler(QObject):
    """ pyQt signal & slots handler"""

    def __init__(self, data_storage):
        super().__init__()
        self.data_storage = data_storage

    @pyqtSlot(tuple)
    def point_added(self, values):
        k = 1
        metric = Metric.EUCLIDEAN
        vote = Vote.SIMPLE
        observation = ObservationFactory.create_observation(values[0], values[1])

        knn = KNNAlghoritm(self.data_storage, k, metric, vote)
        classified_category_id = knn.classify(observation)
        observation.classify(classified_category_id)

        Events.point_classified.emit(observation)

