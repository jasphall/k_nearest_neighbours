import sys

from PyQt5.QtWidgets import QApplication

from domain.knn.knn import KNNAlghoritm
from domain.shared.observation_repository import ObservationRepository
from domain.shared.storage.file_data_storage import FileDataStorage
from infrastructure.events.handlers.events_handler import EventsHandler
from infrastructure.gui.window.appwindow import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SampleDataGenerator().generate_and_export()
    # data_storage = FileDataStorage('../sample_data.txt')
    # data_storage = FileDataStorage('../knn_demonstracyjny_uczacy.txt')
    data_storage = FileDataStorage.EMPTY_STORAGE()
    observation_repository = ObservationRepository(data_storage)
    knn = KNNAlghoritm(data_storage)
    events_handler = EventsHandler(knn)
    window = AppWindow(knn.observation_repository, events_handler)
    window.show()

    sys.exit(app.exec())
