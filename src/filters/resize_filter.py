import cv2
from .base_filter import Filter


class ResizeFilter(Filter):
    def __init__(self, inbound_queue, outbound_queue, scale_factor=0.5):
        super().__init__(inbound_queue, outbound_queue)
        self.scale_factor = scale_factor

    def process(self, frame):
        print("Applying Resize Filter")
        width = int(frame.shape[1] * self.scale_factor)
        height = int(frame.shape[0] * self.scale_factor)
        return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
