from PyQt5.QtCore import QObject


class Event(QObject):
    """ Base event class """

    def __init__(self):
        QObject.__init__(self)
