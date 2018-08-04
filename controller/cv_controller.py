import glob
import cv2
import numpy as np
from modules.preprocess import *

class Controller():

    def __init__(self):
        self.images = self.fetch_images()
        self.img0 = cv2.cvtColor(cv2.imread(self.images[0]), cv2.COLOR_BGR2RGB)
        self.img1 = cv2.cvtColor(cv2.imread(self.images[1]), cv2.COLOR_BGR2RGB)
        self.img_height = 0
        self.img_width = 0
        self.byteValue = 0

        self.lower_rgb = [0, 0, 0]
        self.upper_rgb = [255, 255, 255]

        self.img_color_filt0 = None
        self.img_color_filt1 = None
        self.img_color_filt2 = None

        self.load_values()

    def fetch_images(self, sorted_by='name'):
        if sorted_by == 'name':
            return sorted(glob.glob(r'./images/*.jpg'))
        elif sorted_by == 'time':
            return sorted(glob.glob(r'./images/*.jpg'), key=os.path.getmtime)
        elif sorted_by == 'size':
            return sorted(glob.glob(r'./images/*.jpg'), key=os.path.getsize)
        return glob.glob(r'./images/*.jpg')

    def load_values(self):
        self.img_height, self.img_width, self.byteValue = self.img0.shape
        self.byteValue = self.byteValue * self.img_width

    def update_lower_rgb(self, blue, green, red):
        self.lower_rgb = [blue, green, red]

    def update_upper_rgb(self, blue, green, red):
        self.upper_rgb = [blue, green, red]
        
    def filter(self):
        lower_thresh = np.array(self.lower_rgb)
        upper_thresh = np.array(self.upper_rgb)

        self.img_color_filt0, mask0 = color_filter(self.img0, [lower_thresh, upper_thresh])
        self.img_color_filt1, mask1 = color_filter(self.img1, [lower_thresh, upper_thresh])
    