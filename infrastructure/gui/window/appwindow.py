from PyQt5 import QtCore
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget, QFormLayout

from domain.knn.properties.metric import Metric
from domain.knn.properties.vote import Vote
from infrastructure.events.events import Events
from infrastructure.events.handlers.events_handler import EventsHandler
from infrastructure.gui.canvas.appcanvas import AppCanvas
from infrastructure.gui.color import Color
from infrastructure.gui.elements.gui_element_creator import GuiElementCreator
from infrastructure.utils.collection_utils import CollectionUtils


class AppWindow(QWidget):
    """ Main app window """

    WIDTH = 1100
    HEIGHT = 800
    WINDOW_TITLE = 'k Nearest Neighours'

    CANVAS_WIDTH = 1000
    CANVAS_HEIGHT = 800

    def __init__(self, observation_repository, events_handler, parent=None):
        super().__init__(parent)
        self.observation_repository = observation_repository
        self.events_handler = events_handler

        self.layout = None
        self.left_layout = None
        self.right_layout = None
        self.canvas = None

        self.resize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle(self.WINDOW_TITLE)
        self.configure_gui()
        self.bind_signals_and_slots()

    def configure_gui(self):
        """ GUI layouts configuration """
        self.layout = QHBoxLayout()
        self.left_layout = self.configure_left_layout()
        self.right_layout = self.configure_right_layout()

        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)
        self.setLayout(self.layout)

    def configure_left_layout(self,):
        """ Left layout (canvas) configuration """
        left_layout = QVBoxLayout()
        left_layout.setAlignment(QtCore.Qt.AlignLeft)

        canvas = AppCanvas(self.CANVAS_WIDTH, self.CANVAS_HEIGHT, self)
        canvas.setMinimumSize(self.WIDTH, self.HEIGHT)
        canvas.setMaximumSize(self.WIDTH, self.HEIGHT)

        left_layout.addWidget(canvas)
        self.canvas = canvas

        return left_layout

    def configure_right_layout(self):
        """ Right layout (panel) configuration """
        right_layout = QFormLayout()
        right_layout.setVerticalSpacing(20)

        panel_elements = self.prepare_panel_elements()
        for e in panel_elements:
            right_layout.addRow(e)

        return right_layout

    def prepare_panel_elements(self):
        """ Definition of GUI panel elements """
        title_label = GuiElementCreator.create_label('KNN Alghoritm', GuiElementCreator.header_font())
        k_combobox = GuiElementCreator.create_combobox_with_label([str(i) for i in range(1, 21)], 'Wybierz k')
        metric_combobox = GuiElementCreator.create_combobox_with_label(Metric.get_as_tuple(), 'Wybierz metryke')
        vote_combobox = GuiElementCreator.create_combobox_with_label(Vote.get_as_tuple(), 'Wybierz rodzaj głosowania')
        load_data_button = GuiElementCreator.create_button('Wczytaj dane')

        load_data_button.clicked.connect(self.load_button_clicked)
        k_combobox[1].currentIndexChanged.connect(
            lambda: self.knn_property_changed('k', k_combobox[1].currentIndex()))
        metric_combobox[1].currentIndexChanged.connect(
            lambda: self.knn_property_changed('metric', metric_combobox[1].currentIndex()))
        vote_combobox[1].currentIndexChanged.connect(
            lambda: self.knn_property_changed('vote', vote_combobox[1].currentIndex()))

        elements = [title_label, load_data_button, k_combobox, metric_combobox, vote_combobox]
        return CollectionUtils.unwrap_elements(elements)

    def bind_signals_and_slots(self):
        """ Binding pyQt signals with slots """
        Events.point_added.event.connect(self.events_handler.point_added)
        Events.point_classified.event.connect(self.canvas.point_classified_and_ready_to_draw)
        Events.knn_property_changed.event.connect(self.events_handler.knn_property_changed)

    def load_button_clicked(self):
        """ Load button click event handler """
        categories = self.observation_repository.find_different_categories_num()
        for category_id in categories:
            category_observations = self.observation_repository.find_all_in_given_category(category_id)
            self.canvas.draw_observations(category_observations, Color(category_id), True)

    def knn_property_changed(self, name, value):
        value = int(value)

        if name == 'k':
            value += 1
        if name == 'metric':
            if value == 0:
                value = Metric.EUCLIDEAN
            else:
                value = Metric.TAXICAB
        elif name == 'vote':
            if value == 0:
                value = Vote.SIMPLE
            else:
                value = Vote.REVERSE_DISTANCE_SQUARE

        Events.knn_property_changed.emit((name, value))
