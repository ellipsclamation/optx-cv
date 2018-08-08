import glob
import cv2
import numpy as np
import os
from modules.preprocess import *


class Controller():

    def __init__(self):
        self.images = []
        self.img_index = 0
        self.file_types = ['*.jpg', '*.jpeg', '*.png']

        # Left Image
        self.img0 = None
        self.new_img0 = None
        self.img_height0 = 0
        self.img_width0 = 0
        self.byteValue0 = 0

        # Right Image
        self.img1 = None
        self.new_img1 = None
        self.img_height1 = 0
        self.img_width1 = 0
        self.byteValue1 = 0

        self.lower_color = [0, 0, 0]
        self.upper_color = [255, 255, 255]

        self.modules = []
        self.buttons = []

        self.load_modules()
        self.fetch_images()

    def load_modules(self):
        pass

    def fetch_images(self, path='./images/', sorted_by='name'):
        for file_type in self.file_types:
            if sorted_by == 'name':
                self.images = sorted(self.images + glob.glob(path + file_type))
            elif sorted_by == 'time':
                self.images = sorted(self.images + glob.glob(path + file_type), key=os.path.getmtime)
            elif sorted_by == 'size':
                self.images = sorted(self.images + glob.glob(path + file_type), key=os.path.getsize)
        if self.images:
            self.set_images()

    def set_images(self):
        self.img0 = cv2.cvtColor(cv2.imread(self.images[self.img_index]), cv2.COLOR_BGR2RGB)
        self.img1 = cv2.cvtColor(cv2.imread(self.images[(self.img_index + 1) % len(self.images)]), cv2.COLOR_BGR2RGB)
        self.new_img0 = self.img0
        self.new_img1 = self.img1

        self.load_values()

    def load_values(self):
        self.img_height0, self.img_width0, self.byteValue0 = self.img0.shape
        self.byteValue0 = self.byteValue0 * self.img_width0

        self.img_height1, self.img_width1, self.byteValue1 = self.img1.shape
        self.byteValue1 = self.byteValue1 * self.img_width1

    def cycle_img(self, amount=1):
        amount = amount % len(self.images)
        self.img_index = (self.img_index + amount) % len(self.images)
        self.set_images()
        self.filter()

    def update_lower_color(self, val0, val1, val2):
        self.lower_color = [val0, val1, val2]

    def update_upper_color(self, val0, val1, val2):
        self.upper_color = [val0, val1, val2]

    def filter(self):
        lower_thresh = np.array(self.lower_color)
        upper_thresh = np.array(self.upper_color)

        self.new_img0, mask0 = color_filter(self.img0, [lower_thresh, upper_thresh])
        self.new_img1, mask1 = color_filter(self.img1, [lower_thresh, upper_thresh])
