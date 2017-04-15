from enum import Enum

from PyQt5.QtGui import QColor


class Color(Enum):
    """ Basic colors available in app """
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    WHITE = 4

    def to_qcolor(self):
        if self.name == 'RED':
            return QColor(255, 0, 0)
        elif self.name == 'GREEN':
            return QColor(0, 255, 0)
        elif self.name == 'BLUE':
            return QColor(0, 0, 255)
        elif self.name == 'YELLOW':
            return QColor(255, 255, 0)
        elif self.name == 'WHITE':
            return QColor(0, 0, 0)
