from typing import AnyStr
import cv2


class VideoStream:
    def __init__(self, video_source: AnyStr) -> None:
        self.capture = cv2.VideoCapture(video_source)
        if not self.capture.isOpened():
            raise RuntimeError("Error: Unable to open video source.")
        
    def stream(self) -> cv2.typing.MatLike:
        ret, frame = self.capture.read()
        if not ret:
            raise RuntimeError("Error Capturing the next frame")
        return frame
    
    def __del__(self) -> None:
        self.capture.release()
        