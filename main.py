import cv2
import argparse
from filters import GrayscaleFilter, MirrorFilter, ResizeFilter, EdgeDetectionFilter
from pipeline import Pipeline


def main():
    # Parsing the command line args
    parser = argparse.ArgumentParser(
        description="Real-Time Video Processing with Pipes-and-Filters Pattern"
    )
    parser.add_argument(
        "--video",
        type=str,
        help="Path to the video file. If not provided, webcam will be used.",
    )
    args = parser.parse_args()

    # if the video arg was not provided use the webcam
    if args.video:
        video_source = args.video
        print(f"Using video file: {video_source}")
    else:
        video_source = 0
        print("Using webcam as video source.")

    # Initialize video capture
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Unable to open video source.")
        return

    # Setting the filters
    filters = [
        GrayscaleFilter(),
        MirrorFilter(),
        ResizeFilter(scale_factor=0.5),
        EdgeDetectionFilter(),
    ]

    # Creating the pipeline
    pipeline = Pipeline(filters)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or error.")
            break

        # Processing frame through the pipeline
        processed_frame = pipeline.process(frame)

        # Displaying the processed frame
        cv2.imshow("Processed Video", processed_frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
