import sys
import cv2
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon, QImage, QPainter, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

from controller.cv_controller import Controller


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.controller = Controller()
        self.title = 'CV Tool'

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.main_layout = QVBoxLayout(self)
        self.layouts()
        self.top_section()
        self.bottom_section()
        self.upper_bgr()
        self.bottom_connections()
        self.side_buttons()
        # self.side_section()
        # self.side_connections()

        self.showMaximized()

    def layouts(self):
        self.ll_top = QHBoxLayout()
        self.main_layout.addLayout(self.ll_top)
        self.ll_bot = QHBoxLayout()
        self.main_layout.addLayout(self.ll_bot)
        self.ll_spinners = QGridLayout()
        self.ll_spinners.setHorizontalSpacing(3)
        self.ll_spinners.setHorizontalSpacing(2)
        self.ll_bot.addLayout(self.ll_spinners)
        self.ll_side_buttons = QVBoxLayout()
        self.ll_bot.addLayout(self.ll_side_buttons)

    def top_section(self):
        # self.ll_top = QHBoxLayout()
        # self.main_layout.addLayout(self.ll_top)

        self.display0 = QImage(self.controller.img0, self.controller.img_width, self.controller.img_height, self.controller.byteValue, QImage.Format_RGB888)
        self.display1 = QImage(self.controller.img1, self.controller.img_width, self.controller.img_height, self.controller.byteValue, QImage.Format_RGB888)

        self.pixmap0 = QPixmap(self.display0)
        self.label0 = QLabel()
        self.label0.setPixmap(self.pixmap0)
        self.ll_top.addWidget(self.label0)

        self.pixmap1 = QPixmap(self.display1)
        self.label1 = QLabel()
        self.label1.setPixmap(self.pixmap1)
        self.ll_top.addWidget(self.label1)

    def bottom_section(self):
        # self.ll_spinners = QGridLayout()
        # self.ll_spinners.setHorizontalSpacing(4)
        # self.ll_spinners.setHorizontalSpacing(2)
        # self.main_layout.addLayout(self.ll_spinners)

        # LOWER RED
        self.red_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.red_layout, 0, 0)
        self.red_label = QLabel('LOWER RED')
        self.red_label.setMaximumSize(QtCore.QSize(100, 20))
        self.red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_red = QSpinBox()
        self.spn_red.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_red.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_red.setMinimum(0)
        self.spn_red.setMaximum(255)
        self.spn_red.setSingleStep(1)
        self.spn_red.setProperty('value', 0)
        self.red_layout.addWidget(self.red_label)
        self.red_layout.addWidget(self.spn_red)

        # LOWER GREEN
        self.green_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.green_layout, 0, 1)
        self.green_label = QLabel('LOWER GREEN')
        self.green_label.setMaximumSize(QtCore.QSize(100, 20))
        self.green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_green = QSpinBox()
        self.spn_green.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_green.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_green.setMinimum(0)
        self.spn_green.setMaximum(255)
        self.spn_green.setSingleStep(1)
        self.spn_green.setProperty('value', 0)
        self.green_layout.addWidget(self.green_label)
        self.green_layout.addWidget(self.spn_green)

        # LOWER BLUE
        self.blue_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.blue_layout, 0, 2)
        self.blue_label = QLabel('LOWER BLUE')
        self.blue_label.setMaximumSize(QtCore.QSize(100, 20))
        self.blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_blue = QSpinBox()
        self.spn_blue.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_blue.setMinimum(0)
        self.spn_blue.setMaximum(255)
        self.spn_blue.setSingleStep(1)
        self.spn_blue.setProperty('value', 0)
        self.blue_layout.addWidget(self.blue_label)
        self.blue_layout.addWidget(self.spn_blue)

    def upper_bgr(self):
        # UPPER RED
        self.upper_red_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.upper_red_layout, 1, 0)
        self.upper_red_label = QLabel('UPPER RED')
        self.upper_red_label.setMaximumSize(QtCore.QSize(100, 20))
        self.upper_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_red = QSpinBox()
        self.spn_upper_red.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_upper_red.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_red.setMinimum(0)
        self.spn_upper_red.setMaximum(255)
        self.spn_upper_red.setSingleStep(1)
        self.spn_upper_red.setProperty('value', 255)
        self.upper_red_layout.addWidget(self.upper_red_label)
        self.upper_red_layout.addWidget(self.spn_upper_red)

        # UPPER GREEN
        self.upper_green_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.upper_green_layout, 1, 1)
        self.upper_green_label = QLabel('UPPER GREEN')
        self.upper_green_label.setMaximumSize(QtCore.QSize(100, 20))
        self.upper_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_green = QSpinBox()
        self.spn_upper_green.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_upper_green.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_green.setMinimum(0)
        self.spn_upper_green.setMaximum(255)
        self.spn_upper_green.setSingleStep(1)
        self.spn_upper_green.setProperty('value', 255)
        self.upper_green_layout.addWidget(self.upper_green_label)
        self.upper_green_layout.addWidget(self.spn_upper_green)

        # UPPER BLUE
        self.upper_blue_layout = QVBoxLayout()
        self.ll_spinners.addLayout(self.upper_blue_layout, 1, 2)
        self.upper_blue_label = QLabel('UPPER BLUE')
        self.upper_blue_label.setMaximumSize(QtCore.QSize(100, 20))
        self.upper_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_blue = QSpinBox()
        self.spn_upper_blue.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_upper_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_upper_blue.setMinimum(0)
        self.spn_upper_blue.setMaximum(255)
        self.spn_upper_blue.setSingleStep(1)
        self.spn_upper_blue.setProperty('value', 255)
        self.upper_blue_layout.addWidget(self.upper_blue_label)
        self.upper_blue_layout.addWidget(self.spn_upper_blue)

    def side_buttons(self):
        self.btn_mode = QPushButton('RGB')
        self.btn_mode.setMaximumSize(QtCore.QSize(100, 100))
        self.ll_side_buttons.addWidget(self.btn_mode)

        self.btn_apply = QPushButton('Apply Changes')
        self.btn_apply.setMaximumSize(QtCore.QSize(100, 100))
        self.ll_side_buttons.addWidget(self.btn_apply)

    # def side_section(self):
    #     self.ll_side_buttons_buttons = QVBoxLayout()
    #     self.ll_spinners.addLayout(self.ll_side_buttons_buttons, 0, 3)

    #     self.btn_test = QPushButton('test')
    #     self.ll_side_buttons_buttons.addWidget(self.btn_test)

    def bottom_connections(self):
        self.spn_red.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_green.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_blue.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_upper_red.valueChanged.connect(lambda: self.spinner_update(False))
        self.spn_upper_green.valueChanged.connect(lambda: self.spinner_update(False))
        self.spn_upper_blue.valueChanged.connect(lambda: self.spinner_update(False))

    def spinner_update(self, is_lower):
        if is_lower:
            self.controller.update_lower_bgr(
                self.spn_red.value(),
                self.spn_green.value(),
                self.spn_blue.value()
            )
        else:
            self.controller.update_upper_bgr(
                self.spn_upper_red.value(),
                self.spn_upper_green.value(),
                self.spn_upper_blue.value()
            )
        
        self.controller.filter()

        self.display0 = QImage(
            self.controller.img_color_filt0,
            self.controller.img_width,
            self.controller.img_height,
            self.controller.byteValue,
            QImage.Format_RGB888
        )

        self.pixmap0 = QPixmap(self.display0)
        self.label0.setPixmap(self.pixmap0)

        self.display1 = QImage(
            self.controller.img_color_filt1,
            self.controller.img_width,
            self.controller.img_height,
            self.controller.byteValue,
            QImage.Format_RGB888
        )

        self.pixmap1 = QPixmap(self.display1)
        self.label1.setPixmap(self.pixmap1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = App()

    sys.exit(app.exec_())
