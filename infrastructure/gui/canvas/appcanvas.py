from PyQt5.QtGui import QImage, qRgb, QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget


class AppCanvas(QWidget):
    """ Widget Canvasa do rysowania """

    def __init__(self, width, height, parent=None):
        super().__init__(parent)

        if width <= 0 or height <= 0:
            raise ValueError('Size cannot be less than 0')
        self.width = width
        self.height = height
        self.img = AppCanvasImage(width, height, QImage.Format_RGB32, qRgb(0, 0, 0), self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.img)


class AppCanvasImage(QImage):

    def __init__(self, width, height, format, bg_color, parent=None):
        super().__init__(width, height, format)
        self.fill(bg_color)

