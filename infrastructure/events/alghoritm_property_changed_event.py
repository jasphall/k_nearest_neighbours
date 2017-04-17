from PyQt5.QtCore import pyqtSignal

from infrastructure.events.event import Event


class AlghoritmPropertyChangedEvent(Event):
    event = pyqtSignal(tuple)

    def emit(self, data):
        self.event.emit(data)