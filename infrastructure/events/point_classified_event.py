from PyQt5.QtCore import pyqtSignal

from domain.shared.observation import Observation
from domain.shared.observation_container import ObservationContainer
from infrastructure.events.event import Event


class PointClassifiedEvent(Event):
    event = pyqtSignal(ObservationContainer)

    def emit(self, observation_container):
        self.event.emit(observation_container)
        print('PointClassifiedEvent emitted')
