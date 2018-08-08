from modules.module import Module
from PyQt5.QtWidgets import QPushButton


class RGB(Module):

    def __init__(self):
        self.button = QPushButton('RGB')
        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]
        self.lower_label0 = 'Lower Red'
        self.lower_label1 = 'Lower Green'
        self.lower_label2 = 'Lower Blue'
        self.upper_label0 = 'Upper Red'
        self.upper_label1 = 'Upper Green'
        self.upper_label2 = 'Upper Blue'

    def btn_clicked(self):
        pass

    def process(self, image, lower_color, upper_color):
        pass
