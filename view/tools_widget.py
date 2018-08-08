from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QSpinBox
from PyQt5 import QtCore


class Tools:

    def __init__(self, layouts, controller, display):
        self.layouts = layouts
        self.controller = controller
        self.display = display

        self.initUI()

    def initUI(self):
        self.color_spinners()
        self.spinner_connections()
        self.nav_buttons()
        self.nav_buttons_connections()

    def color_spinners(self):
        # LOWER RED
        self.lower_red_layout = QVBoxLayout()
        self.layouts.ll_spinners.addLayout(self.lower_red_layout, 0, 0)
        self.lower_red_label = QLabel('Lower Red')
        self.lower_red_label.setMaximumSize(QtCore.QSize(100, 20))
        self.lower_red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_red = QSpinBox()
        self.spn_lower_red.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_lower_red.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_red.setMinimum(0)
        self.spn_lower_red.setMaximum(255)
        self.spn_lower_red.setSingleStep(1)
        self.spn_lower_red.setProperty('value', 0)
        self.lower_red_layout.addWidget(self.lower_red_label)
        self.lower_red_layout.addWidget(self.spn_lower_red)

        # LOWER GREEN
        self.lower_green_layout = QVBoxLayout()
        self.layouts.ll_spinners.addLayout(self.lower_green_layout, 0, 1)
        self.lower_green_label = QLabel('Lower Green')
        self.lower_green_label.setMaximumSize(QtCore.QSize(100, 20))
        self.lower_green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_green = QSpinBox()
        self.spn_lower_green.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_lower_green.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_green.setMinimum(0)
        self.spn_lower_green.setMaximum(255)
        self.spn_lower_green.setSingleStep(1)
        self.spn_lower_green.setProperty('value', 0)
        self.lower_green_layout.addWidget(self.lower_green_label)
        self.lower_green_layout.addWidget(self.spn_lower_green)

        # LOWER BLUE
        self.lower_blue_layout = QVBoxLayout()
        self.layouts.ll_spinners.addLayout(self.lower_blue_layout, 0, 2)
        self.lower_blue_label = QLabel('Lower Blue')
        self.lower_blue_label.setMaximumSize(QtCore.QSize(100, 20))
        self.lower_blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_blue = QSpinBox()
        self.spn_lower_blue.setMaximumSize(QtCore.QSize(100, 80))
        self.spn_lower_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_lower_blue.setMinimum(0)
        self.spn_lower_blue.setMaximum(255)
        self.spn_lower_blue.setSingleStep(1)
        self.spn_lower_blue.setProperty('value', 0)
        self.lower_blue_layout.addWidget(self.lower_blue_label)
        self.lower_blue_layout.addWidget(self.spn_lower_blue)

        # UPPER RED
        self.upper_red_layout = QVBoxLayout()
        self.layouts.ll_spinners.addLayout(self.upper_red_layout, 1, 0)
        self.upper_red_label = QLabel('Upper Red')
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
        self.layouts.ll_spinners.addLayout(self.upper_green_layout, 1, 1)
        self.upper_green_label = QLabel('Upper Green')
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
        self.layouts.ll_spinners.addLayout(self.upper_blue_layout, 1, 2)
        self.upper_blue_label = QLabel('Upper Blue')
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

    def nav_buttons(self):
        self.btn_up = QPushButton('Up')
        self.btn_up.setMaximumSize(QtCore.QSize(100, 100))
        self.layouts.ll_spinners.addWidget(self.btn_up, 0, 3)

        self.btn_down = QPushButton('Down')
        self.btn_down.setMaximumSize(QtCore.QSize(100, 100))
        self.layouts.ll_spinners.addWidget(self.btn_down, 1, 3)

    def nav_buttons_connections(self):
        self.btn_up.clicked.connect(lambda: self.button_update(-1))
        self.btn_down.clicked.connect(lambda: self.button_update(1))

    def spinner_connections(self):
        self.spn_lower_red.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_lower_green.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_lower_blue.valueChanged.connect(lambda: self.spinner_update(True))
        self.spn_upper_red.valueChanged.connect(lambda: self.spinner_update(False))
        self.spn_upper_green.valueChanged.connect(lambda: self.spinner_update(False))
        self.spn_upper_blue.valueChanged.connect(lambda: self.spinner_update(False))

    def button_update(self, amount=1):
        self.controller.cycle_img(amount)
        self.display.update_display()

    def spinner_update(self, is_lower):
        if is_lower:
            self.controller.update_lower_color(
                self.spn_lower_red.value(),
                self.spn_lower_green.value(),
                self.spn_lower_blue.value()
            )
        else:
            self.controller.update_upper_color(
                self.spn_upper_red.value(),
                self.spn_upper_green.value(),
                self.spn_upper_blue.value()
            )

        self.controller.filter()
        self.display.update_display()
