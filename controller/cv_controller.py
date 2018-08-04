import cv2
import numpy as np
from modules.preprocess import *

class Controller():

    def __init__(self):
        self.img0 = cv2.cvtColor(cv2.imread(r'./images/0.jpg'), cv2.COLOR_BGR2RGB)
        self.img1 = cv2.cvtColor(cv2.imread(r'./images/1.jpg'), cv2.COLOR_BGR2RGB)
        self.img_height = 0
        self.img_width = 0
        self.byteValue = 0

        self.lower_bgr = [0, 0, 0]
        self.upper_bgr = [255, 255, 255]

        self.img_color_filt0 = None
        self.img_color_filt1 = None
        self.img_color_filt2 = None

        self.load_values()

    def load_values(self):
        self.img_height, self.img_width, self.byteValue = self.img0.shape
        self.byteValue = self.byteValue * self.img_width

    def update_lower_bgr(self, blue, green, red):
        self.lower_bgr = [blue, green, red]

    def update_upper_bgr(self, blue, green, red):
        self.upper_bgr = [blue, green, red]
        
    def filter(self):
        lower_thresh = np.array(self.lower_bgr)
        upper_thresh = np.array(self.upper_bgr)

        self.img_color_filt0, mask0 = color_filter(self.img0, [lower_thresh, upper_thresh])
        self.img_color_filt1, mask1 = color_filter(self.img1, [lower_thresh, upper_thresh])
    