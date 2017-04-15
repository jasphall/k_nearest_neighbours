from PyQt5.QtWidgets.QWidget import QWidget


class AppWindow(QWidget):
    """ Główne okno aplikacji """

    def __init__(self, parent=None):
        super().__init__(parent)