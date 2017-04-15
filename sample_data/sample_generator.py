from PyQt5.QtGui import QColor


class SampleDataGenerator(object):

    CLUSTER_SIZE = 10
    CLUSTER_1_COLOR = QColor(255, 0, 0)
    CLUSTER_2_COLOR = QColor(0, 0, 255)
    CLUSTER_3_COLOR = QColor(255, 255, 0)
    CLUSTER_4_COLOR = QColor(255, 0, 255)

    def generate_and_export(self):
        data = self.generate()
        self.export_to_file(data)

    def generate(self):
        data = []
        x_offset = 200
        y_offset = 200
        for i in range(0, 4):
            if i == 2:
                y_offset += 200
                x_offset = 200
            for j in range(0, 10):
                for k in range(0, 15):
                    data.append((x_offset + j*20, y_offset + k*10, i))
            x_offset += 300

        return data

    def export_to_file(self, data):
        f = open('../sample_data.txt', 'w')
        for row in data:
            f.write(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + '\n')
        f.close()
