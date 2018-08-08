from abc import ABC, abstractmethod


class Module(ABC):

    @abstractmethod
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]
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

        @abstractmethod
        def btn_clicked(self):
            pass

        @abstractmethod
        def process(self, image, lower_color, upper_color):
            pass
