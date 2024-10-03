import cv2
from .base_filter import Filter


class MirrorFilter(Filter):
    def process(self, frame):
        print("Applying Mirror Filter")
        return cv2.flip(frame, 1)
