import glob
import cv2
import numpy as np
from modules.preprocess import *

class Controller():

    def __init__(self):
        self.images = None
        self.img0 = None
        self.img1 = None

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
        self.img_color_filt2 = None

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
            self.load_values()

    def set_images(self):
        self.img0 = cv2.cvtColor(cv2.imread(self.images[0]), cv2.COLOR_BGR2RGB)
        try:
            self.img1 = cv2.cvtColor(cv2.imread(self.images[1]), cv2.COLOR_BGR2RGB)
        except IndexError:
            return

    def load_values(self):
        self.img_height0, self.img_width0, self.byteValue0 = self.img0.shape
        self.byteValue0 = self.byteValue0 * self.img_width0

        try:
            self.img_height1, self.img_width1, self.byteValue1 = self.img1.shape
            self.byteValue1 = self.byteValue1 * self.img_width1
        except AttributeError:
            return

    def update_lower_rgb(self, blue, green, red):
        self.lower_rgb = [blue, green, red]

    def update_upper_rgb(self, blue, green, red):
        self.upper_rgb = [blue, green, red]
        
    def filter(self):
        lower_thresh = np.array(self.lower_rgb)
        upper_thresh = np.array(self.upper_rgb)

        self.img_color_filt0, mask0 = color_filter(self.img0, [lower_thresh, upper_thresh])
        if self.img1:
            self.img_color_filt1, mask1 = color_filter(self.img1, [lower_thresh, upper_thresh])
