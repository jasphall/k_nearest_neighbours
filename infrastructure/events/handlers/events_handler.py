from PyQt5.QtCore import pyqtSlot, QObject

from domain.shared.observation import ObservationFactory, Observation
from domain.shared.observation_container import ObservationContainer
from infrastructure.events.events import Events


class EventsHandler(QObject):
    """ pyQt signal & slots handler"""

    def __init__(self, knn):
        super().__init__()
        self.knn = knn

    @pyqtSlot(Observation)
    def point_added(self, observation):
        classified_category_id, neighbours = self.knn.classify(observation)
        observation.classify(classified_category_id)

        Events.point_classified.emit(ObservationContainer(observation, neighbours))

    @pyqtSlot(tuple)
    def knn_property_changed(self, data):
        if data[0] == 'k':
            print('Changed knn k parameter to: ' + str(data[1]))
            self.knn.setup_k(data[1])
        elif data[0] == 'metric':
            print('Changed knn metric parameter to: ' + str(data[1]))
            self.knn.setup_metric(data[1])
        elif data[0] == 'vote':
            print('Changed knn vote parameter to: ' + str(data[1]))
            self.knn.setup_vote(data[1])

