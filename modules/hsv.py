from modules.module import Module
from PyQt5.QtWidgets import QPushButton

class HSV(Module):

    def __init__(self):
        self.button = QPushButton('HSV')
        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]
        self.lower_label0 = 'Lower Hue'
        self.lower_label1 = 'Lower Saturation'
        self.lower_label2 = 'Lower Value'
        self.upper_label0 = 'Upper Hue'
        self.upper_label1 = 'Upper Saturation'
        self.upper_label2 = 'Upper Value'

    def btn_clicked(self):
        pass

    def process(self, image, lower_color, upper_color):
        pass