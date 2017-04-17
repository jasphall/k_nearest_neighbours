from PyQt5.QtCore import pyqtSignal

from infrastructure.events.event import Event


class PointAddedEvent(Event):
    event = pyqtSignal(tuple)

    def emit(self, values):
        self.event.emit(values)