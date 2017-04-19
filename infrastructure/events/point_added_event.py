from PyQt5.QtCore import pyqtSignal

from domain.shared.observation import Observation
from infrastructure.events.event import Event


class PointAddedEvent(Event):
    event = pyqtSignal(Observation)

    def emit(self, o):
        self.event.emit(o)