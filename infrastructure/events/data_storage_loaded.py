from PyQt5.QtCore import pyqtSignal

from infrastructure.events.event import Event


class DataStorageLoadedEvent(Event):
    """ Event emitted when user loads a new file into datastorage """
    event = pyqtSignal(str)

    def emit(self, name):
        self.event.emit(name)
        print('DataStorageLoadedEvent emitted')
