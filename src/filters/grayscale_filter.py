import cv2
from .base_filter import Filter


class GrayscaleFilter(Filter):
    def process(self, frame):
        print("Applying Grayscale Filter")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
