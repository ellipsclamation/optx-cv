import glob
import cv2
import numpy as np
import os
from modules.preprocess import *


class Controller():

    def __init__(self):
        self.images = None
        self.img0 = None
        self.img1 = None
        self.img_index = 0

        self.img_height0 = 0
        self.img_width0 = 0
        self.byteValue0 = 0

        self.img_height1 = 0
        self.img_width1 = 0
        self.byteValue1 = 0

        self.lower_rgb = [0, 0, 0]
        self.upper_rgb = [255, 255, 255]

        self.img_color_filt0 = None
        self.img_color_filt1 = None

        self.fetch_images()

    def fetch_images(self, path='./images/', sorted_by='name'):
        if sorted_by == 'name':
            self.images = sorted(glob.glob(path + '*.jpg'))
        elif sorted_by == 'time':
            self.images = sorted(glob.glob(path + '*.jpg'), key=os.path.getmtime)
        elif sorted_by == 'size':
            self.images = sorted(glob.glob(path + '*.jpg'), key=os.path.getsize)
        if self.images:
            self.set_images()
            # self.load_values()

    def set_images(self):
        self.img0 = cv2.cvtColor(cv2.imread(self.images[self.img_index]), cv2.COLOR_BGR2RGB)
        self.img1 = cv2.cvtColor(cv2.imread(self.images[(self.img_index + 1) % len(self.images)]), cv2.COLOR_BGR2RGB)

        self.load_values()

    def load_values(self):
        self.img_height0, self.img_width0, self.byteValue0 = self.img0.shape
        self.byteValue0 = self.byteValue0 * self.img_width0

        try:
            self.img_height1, self.img_width1, self.byteValue1 = self.img1.shape
            self.byteValue1 = self.byteValue1 * self.img_width1
        except AttributeError:
            return

    def cycle_img(self, amount=1):
        amount = amount % len(self.images)
        self.img_index = (self.img_index + amount) % len(self.images)
        self.set_images()
        self.filter()

    def update_lower_rgb(self, red, green, blue):
        self.lower_rgb = [red, green, red]

    def update_upper_rgb(self, red, green, blue):
        self.upper_rgb = [red, green, red]

    def filter(self):
        lower_thresh = np.array(self.lower_rgb)
        upper_thresh = np.array(self.upper_rgb)

        self.img_color_filt0, mask0 = color_filter(self.img0, [lower_thresh, upper_thresh])
        self.img_color_filt1, mask1 = color_filter(self.img1, [lower_thresh, upper_thresh])
