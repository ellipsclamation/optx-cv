from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QPushButton


class Module(ABC):

    @abstractmethod
    def __init__(self):
        self.button = QPushButton('')
        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]
        self.lower_label0 = ''
        self.lower_label1 = ''
        self.lower_label2 = ''
        self.upper_label0 = ''
        self.upper_label1 = ''
        self.upper_label2 = ''
        super().__init__()

        def set_color(self, lower_color, upper_color):
            """
            set lower and upper color for module

            Args:
                lower_color (list of int): A list of 3 int for lower value
                upper_color (list of int): A list of 3 int for upper value
            """
            self.lower_color = lower_color
            self.upper_color = upper_color

        def get_color(self):
            """
            gets lower and upper color for module

            Returns:
                lower_color (list of int): A list of 3 int for lower value
                upper_color (list of int): A list of 3 int for upper value
            """
            return self.lower_color, self.upper_color

        def get_labels(self):
            return [self.lower_label0, self.lower_label1, self.lower_label2],
            [self.upper_label0, self.upper_label1, self.upper_label2]

        @abstractmethod
        def btn_clicked(self):
            pass

        @abstractmethod
        def process(self, image, lower_color, upper_color):
            pass
