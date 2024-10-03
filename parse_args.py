import argparse

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