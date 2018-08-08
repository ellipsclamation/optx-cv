import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from view.main_view import MainView
from controller.controller import Controller


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.controller = Controller()
        self.title = 'optx - opencv pre-processing tool'

        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 720

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.main_layout = QVBoxLayout(self)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.main_view = MainView(self, self.main_layout, self.controller)

        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = App()

    sys.exit(app.exec_())
