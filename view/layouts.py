from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout


class Layouts:

    def __init__(self, main_layout):
        self.main_layout = main_layout
        self.ll_top = QHBoxLayout()  # top half to display images
        self.ll_bot = QHBoxLayout()  # bottom half to display buttons
        self.ll_spinners = QGridLayout()  # bottom, grid layout for spinners and nav btns
        self.ll_side_buttons = QVBoxLayout()  # bottom, layout for module btns

        self.add_layouts()

    def add_layouts(self):
        self.main_layout.addLayout(self.ll_top)
        self.main_layout.addLayout(self.ll_bot)
        self.ll_spinners.setHorizontalSpacing(4)
        self.ll_spinners.setHorizontalSpacing(2)
        self.ll_bot.addLayout(self.ll_spinners)
        self.ll_bot.addLayout(self.ll_side_buttons)
