import sys

from PyQt5.QtWidgets import QApplication

from domain.shared.observation_repository import ObservationRepository
from domain.shared.storage.file_data_storage import FileDataStorage
from infrastructure.gui.window.appwindow import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SampleDataGenerator().generate_and_export()
    data_storage = FileDataStorage('../sample_data.txt')
    observation_repository = ObservationRepository(data_storage)
    window = AppWindow(observation_repository)
    window.show()

    sys.exit(app.exec())
