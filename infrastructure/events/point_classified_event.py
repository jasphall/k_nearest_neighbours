from PyQt5.QtCore import pyqtSignal

from domain.shared.observation import Observation
from infrastructure.events.event import Event


class PointClassifiedEvent(Event):
    event = pyqtSignal(Observation)

    def emit(self, observation):
        self.event.emit(observation)
        print('PointClassifiedEvent emitted')
