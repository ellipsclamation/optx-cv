from modules.module import Module
from PyQt5.QtWidgets import QPushButton

class Filter_Contours(Module):

    def __init__(self):
        self.min_cont_size = 10
        self.max_cont_size = 2000
        self.new_cont_list = []

        # TODO need to implement filter contours
        
        # for cont in frame_contours:
        #     cont_len = len(cont)
        #     if ( (cont_len > min_cont_size) and (cont_len < max_cont_size) ):
        #         new_cont_list.append(cont)
        # filtered_contours = np.array(new_cont_list)
        # return filtered_contours