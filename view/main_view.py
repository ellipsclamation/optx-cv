from PyQt5.QtWidgets import QVBoxLayout, QFileDialog, QPushButton
from PyQt5 import QtCore

from view.layouts import Layouts
from view.display_widget import Display
from view.tools_widget import Tools


class MainView:

    def __init__(self, window, main_layout, controller):
        self.window = window
        self.main_layout = main_layout
        self.controller = controller

        self.layouts = None
        self.initUI()

    def initUI(self):
        if not self.controller.images:
            self.load_images()
        else:
            self.loadUI()

    def load_images(self):
        self.ll_prompt = QVBoxLayout()
        self.main_layout.addLayout(self.ll_prompt)
        self.btn_load_img = QPushButton('Load Image Folder')
        self.btn_load_img.setMaximumSize(QtCore.QSize(1920, 100))
        self.ll_prompt.addWidget(self.btn_load_img)
        self.btn_load_img.clicked.connect(self.directory_dialog)

    def directory_dialog(self):
        directory = str(QFileDialog.getExistingDirectory(self.window, "Select Directory")) + '/'
        self.controller.fetch_images(directory)
        if self.controller.images:
            self.loadUI()
            self.remove_prompt()

    def remove_prompt(self):
        self.ll_prompt.removeWidget(self.btn_load_img)
        self.btn_load_img.deleteLater()
        self.btn_load_img = None

    def loadUI(self):
        self.layouts = Layouts(self.main_layout)
        self.display = Display(self.layouts, self.controller)
        self.tools = Tools(self.layouts, self.controller, self.display)
