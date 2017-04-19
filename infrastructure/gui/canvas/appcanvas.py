from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QMouseEvent
from PyQt5.QtWidgets import QWidget

from domain.shared.observation import Observation
from domain.shared.observation_container import ObservationContainer
from infrastructure.events.events import Events
from infrastructure.gui.color import Color


class AppCanvas(QWidget):
    """ Canvas widget for drawing """

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

    def mousePressEvent(self, event: QMouseEvent):
        """ Mouse press event handler """
        Events.point_added.emit((event.x(), event.y()))

    def draw_observations(self, values, color, circle_shape=False):
        if circle_shape is False:
            self.img.draw_points(values, color.to_qcolor())
        else:
            self.img.draw_circle_points(values, color.to_qcolor())
        self.repaint()

    @pyqtSlot(ObservationContainer)
    def point_classified_and_ready_to_draw(self, observation_container):
        observation = observation_container.observation
        neighbours = observation_container.neighbours

        self.draw_observations([observation], Color(observation.category_id))
        self.draw_observations(neighbours, Color.WHITE, circle_shape=True)
        print('PointClassifiedEvent reveived')


class AppCanvasImage(QImage):

    def __init__(self, width, height, format, bg_color, parent=None):
        super().__init__(width, height, format)
        self.width = width
        self.height = height
        self.painter = QPainter(self)
        self.fill(bg_color)
        self.draw_axes(width/2, height/2, Color.WHITE)

    def draw_axes(self, x, y, color):
        painter = self.painter
        pen = QPen(color.to_qcolor())
        pen.setWidth(1)
        painter.setPen(pen)

        painter.drawLine(x, 0, x, self.height)
        painter.drawLine(0, y, self.width, y)

    def draw_point(self, x, y, color):
        painter = self.painter
        pen = QPen(color)
        pen.setWidth(5)
        painter.setPen(pen)

        painter.drawPoint(x, y)

    def draw_points(self, points, color):
        for p in points:
            self.draw_point(p.x, p.y, color)

    def draw_circle_point(self, x, y, color):
        painter = self.painter
        pen = QPen(color)
        pen.setWidth(5)
        painter.setPen(pen)

        painter.drawEllipse(x, y, 5, 5)

    def draw_circle_points(self, points, color):
        for p in points:
            self.draw_circle_point(p.x, p.y, color)