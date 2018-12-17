import cv2
import numpy as np
import backend

#import module

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()
 
    def get_frame(self):
        return backend.load(self, imagename="Template1", save="webcam1")
    
    def get_frame2(self):
        return backend.load(self, imagename="Template2", save="webcam2")

    def get_frame3(self):
        return backend.load(self, imagename="Template3", save="webcam3")

    def get_frame4(self):
        return backend.load(self, imagename="Template4", save="webcam4")

    def get_frame5(self):
        return backend.load(self, imagename="Template5", save="webcam5")

    def get_image(self):
        return backend.loadpic(self, imagename="goodjob")

    def get_default(self):
        return backend.default(self)

    def get_start(self):
        return backend.loadpic(self, imagename="Hello")

    def get_starting(self):
        return backend.loadpic(self, imagename="Starting")

    def get_end(self):
        return backend.loadpic(self, imagename="End")

    def get_saygoodbye(self):
        return backend.loadpic(self, imagename="Saygoodbye")



