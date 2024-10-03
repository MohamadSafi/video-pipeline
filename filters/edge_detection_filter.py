import cv2
from .base_filter import Filter


class EdgeDetectionFilter(Filter):
    def process(self, frame):
        print("Applying Edge Detection Filter")
        return cv2.Canny(frame, 100, 200)
