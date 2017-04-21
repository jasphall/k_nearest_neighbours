from PyQt5.QtCore import pyqtSignal

from infrastructure.events.event import Event


class ClearCanvasEvent(Event):
    """ Event emitted when there is a need to clear canvas image """
    event = pyqtSignal()

    def emit(self):
        self.event.emit()
        print('ClearCanvasEvent emitted')
