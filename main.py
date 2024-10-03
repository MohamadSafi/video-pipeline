import cv2
import argparse
from src.filters import GrayscaleFilter, MirrorFilter, ResizeFilter, EdgeDetectionFilter
from src import Pipeline, VideoStream


def parse_args():
    parser = argparse.ArgumentParser(
        description="Real-Time Video Processing with Pipes-and-Filters Pattern"
    )
    parser.add_argument(
        "--video",
        type=str,
        help="Path to the video file. If not provided, webcam will be used.",
        default=0
    )
    args = parser.parse_args()
    if isinstance(args.video, str):
        print(f"Using video file: {args.video}")
    else:
        print("Using webcam as video source.")
    return args

def run_app(args):
    video_stream = VideoStream(args.video)
    filters = [
        GrayscaleFilter(),
        MirrorFilter(),
        ResizeFilter(scale_factor=0.5),
        EdgeDetectionFilter(),
    ]
    pipeline = Pipeline(filters)
    while True:
        frame = video_stream.stream()
        processed_frame = pipeline.process(frame)
        cv2.imshow("Processed Video", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

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
