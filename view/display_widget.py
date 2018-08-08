from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap


class Display:

    def __init__(self, layouts, controller, window):
        self.layouts = layouts
        self.controller = controller
        self.window = window

        self.display0 = QImage()
        self.display1 = QImage()

        self.initUI()

    def initUI(self):
        self.create_display()

    def create_display(self):
        self.label0 = QLabel()
        self.label0.setMaximumSize(
            int(self.window.frameGeometry().width()/2),
            int(self.window.frameGeometry().height()/2)
        )
        self.label0.setScaledContents(True)
        self.layouts.ll_top.addWidget(self.label0)

        self.label1 = QLabel()
        self.label1.setMaximumSize(
            int(self.window.frameGeometry().width()/2),
            int(self.window.frameGeometry().height()/2)
        )
        self.label1.setScaledContents(True)
        self.layouts.ll_top.addWidget(self.label1)

        self.update_display()

    def update_display(self):
        self.display0 = QImage(
            self.controller.new_img0,
            self.controller.img_width0,
            self.controller.img_height0,
            self.controller.byteValue0,
            QImage.Format_RGB888
        )

        self.display1 = QImage(
            self.controller.new_img1,
            self.controller.img_width1,
            self.controller.img_height1,
            self.controller.byteValue1,
            QImage.Format_RGB888
        )
        self.pixmap0 = QPixmap(self.display0)
        self.pixmap1 = QPixmap(self.display1)
        self.label0.setPixmap(self.pixmap0)
        self.label1.setPixmap(self.pixmap1)
