from modules.module import Module


class RGB(Module):

    def __init__(self, name='RGB', text='RGB'):
        self.name = name
        self.text = text
        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]

    def btn_clicked(self):
        pass

    def process(self, image, lower_color, upper_color):
        pass
