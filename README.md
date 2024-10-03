# Real-Time Video Processing with Pipes-and-Filters Pattern

This project implements the pipes-and-filters architectural pattern to process video streams in real time. It reads video input from a webcam or a video file, applies a sequence of filters to each frame, and displays the processed output.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Available Filters](#available-filters)

## Features

- **Real-Time Processing**: Applies filters to video frames in real time.
- **Modular Design**: Easily add, remove, or modify filters.
- **Flexible Input**: Supports both webcam and video file inputs.
- **Extensibility**: Designed to allow for new filters to be added with minimal effort.

## Project Structure

```
video_pipeline/
├── README.md
├── filters
├── main.py
├── parse_args.py
├── requirements.txt
└── src
    ├── __init__.py
    ├── filters
    │   ├── __init__.py
    │   ├── base_filter.py
    │   ├── edge_detection_filter.py
    │   ├── grayscale_filter.py
    │   ├── mirror_filter.py
    │   └── resize_filter.py
    ├── pipeline.py
    └── video_stream.py
```


- **src/filters/**: Contains individual filter classes.
- **src/pipeline.py**: Contains the `Pipeline` class.
- **parse_args.py**: Handling the passed arguments.
- **video_stream.py**: Contains VideoStream for processing frames.
- **main.py**: The main application script.
- **requirements.txt**: Python dependencies.
- **README.md**: Project documentation.

## Installation

### Prerequisites

- Python 3.x
- pip package manager

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/MohamadSafi/video-pipeline.git
cd video_pipeline
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage
### Running the Application with Webcam
```bash
python main.py
```

### Running the Application with a Video File
```bash
python main.py --video path/to/your/video.mp4
```

## Available Filters
1. **Grayscale Filter**

    - Description: Converts the frame to grayscale.
    - File: `filters/grayscale_filter.py`

2. **Mirror Filter**

    - Description: Mirrors the frame horizontally.
    - File: `filters/mirror_filter.py`

3. **Resize Filter**

    - Description: Resizes the frame to half its original size.
    - File: `filters/resize_filter.py`

4. **Edge Detection Filter**

    - Description: Highlights edges using the Canny edge detection algorithm.
    - File: `filters/edge_detection_filter.py`
  
## Demo Video


<a href="https://youtu.be/iYwJzqkvv0A">
    <img src="https://i.ibb.co/CQfZJ39/demo.png" alt="Demo video" width="100" />
</a>

