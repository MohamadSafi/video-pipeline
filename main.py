import cv2
from parse_args import parse_args
from src import Pipeline, VideoStream
from src.filters import GrayscaleFilter, MirrorFilter, ResizeFilter, EdgeDetectionFilter
from multiprocessing import Queue

source_pipe = Queue()
sink_pipe = Queue()

def run_pipeline():
    mirror_queue, resize_queue, edge_detection_queue = Queue(), Queue(), Queue()
    filters = [
        GrayscaleFilter(source_pipe, mirror_queue),
        MirrorFilter(mirror_queue, resize_queue),
        ResizeFilter(resize_queue, edge_detection_queue, scale_factor=0.5),
        EdgeDetectionFilter(edge_detection_queue, sink_pipe)
    ]
    pipeline = Pipeline(filters)
    pipeline.run_background()

def run_app(args):
    video_stream = VideoStream(args.video)
    run_pipeline()
    while True:
        frame = video_stream.stream()
        source_pipe.put(frame)
        processed_frame = sink_pipe.get()
        if processed_frame is None:
            break
        cv2.imshow("Processed Video", processed_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            return

def main():
    args = parse_args()
    try:
        run_app(args)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
