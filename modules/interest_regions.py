from modules.module import Module
from PyQt5.QtWidgets import QPushButton

class InterestRegions(Module):

    def __init__(self):
        self.button = QPushButton('Interest Regions')
        self.roi_size = 1000
        

        # TODO need to implement interest regions
        # interest regions will use all of the preprocessing and filter
        # techniques used during RoboSub
        
        # color_filt_frame, mask = preprocess(frame) # color filtering

        # grayscale_frame = cv2.cvtColor(color_filt_frame, cv2.COLOR_BGR2GRAY) # to grayscale

        # ret, thresh_frame = cv2.threshold(grayscale_frame, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # frame_c, frame_contours, frame_heirarchy = cv2.findContours(thresh_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # filtered_contours = filter_contours(frame_contours) # filter the contours based on size

        # boxes = [cv2.boundingRect(c) for c in filtered_contours] # make boxes around contours
        # interest_regions = [b for b in boxes if b[2]*b[3] > roi_size]

        # return interest_regions