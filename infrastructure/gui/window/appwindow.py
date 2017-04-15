from PyQt5 import QtCore
from PyQt5.QtWidgets import QHBoxLayout, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget, QFormLayout

from domain.knn.properties.metric import Metric
from domain.knn.properties.vote import Vote
from infrastructure.gui.canvas.appcanvas import AppCanvas
from infrastructure.gui.elements.gui_element_creator import GuiElementCreator
from infrastructure.utils.collection_utils import CollectionUtils


class AppWindow(QWidget):
    """ Główne okno aplikacji """

    WIDTH = 1100
    HEIGHT = 800
    WINDOW_TITLE = 'k Neirest Neighours'

    CANVAS_WIDTH = 1000
    CANVAS_HEIGHT = 800

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = None
        self.left_layout = None
        self.right_layout = None
        self.canvas = None

        self.resize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle(self.WINDOW_TITLE)
        self.configure_gui()

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

        elements = [title_label, load_data_button, k_combobox, metric_combobox, vote_combobox]
        return CollectionUtils.unwrap_elements(elements)

    def load_button_clicked(self):
        """ Event handler for load button click action """
        filename = QFileDialog.getOpenFileName(self, 'Wczytaj plik', '/')
        print(filename)
