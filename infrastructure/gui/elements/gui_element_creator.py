from PyQt5 import QtGui

from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox


class GuiElementCreator(object):

    @staticmethod
    def base_font():
        font = QtGui.QFont()
        font.setFamily('Lucida')
        font.setFixedPitch(True)
        font.setPointSize(10)
        return font

    @staticmethod
    def header_font():
        font = GuiElementCreator.base_font()
        font.setPointSize(14)
        return font

    @staticmethod
    def create_button(label):
        button = QPushButton(label)
        return button

    @staticmethod
    def create_label(label, font):
        l = QLabel(label)
        l.setFont(font)
        return l

    @staticmethod
    def create_combobox(values):
        combo_box = QComboBox()
        combo_box.addItems(values)
        return combo_box

    @staticmethod
    def create_button_with_label(button_label, label):
        l = GuiElementCreator.create_label(label, GuiElementCreator.base_font())
        b = GuiElementCreator.create_button(button_label)
        return [l, b]

    @staticmethod
    def create_combobox_with_label(values, label):
        l = GuiElementCreator.create_label(label, GuiElementCreator.base_font())
        b = GuiElementCreator.create_combobox(values)
        return [l, b]
