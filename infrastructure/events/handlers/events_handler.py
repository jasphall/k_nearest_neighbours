from PyQt5.QtCore import pyqtSlot, QObject


class EventsHandler(QObject):
    """ pyQt signal & slots handler"""

    @pyqtSlot(tuple)
    def point_added(self, values):
        print(values)
        pass
