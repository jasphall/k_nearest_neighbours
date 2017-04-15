import sys

from PyQt5.QtWidgets import QApplication

from infrastructure.gui.window.appwindow import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()

    sys.exit(app.exec())
