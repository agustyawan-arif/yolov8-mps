# YOLOv8 Object Detection with Flask and Streamlit

This repository contains a Python application that performs object detection using the YOLOv8 medium model. The application uses Flask for the backend API and Streamlit for the frontend interface. It also demonstrates the performance comparison between a standard CPU and the Apple M2 chip.

## Overview

### Performance Comparison

We tested the inference speeds using two setups: a standard CPU and the Apple M2 chip.

#### CPU Results:

- **Inference Speed:** ~140ms per image
- **Example Output:**
  - Confidence: 0.95, Class: person
  - Confidence: 0.88, Class: bottle
  - Speed: 1.1ms preprocess, 142.5ms inference, 0.6ms postprocess

#### Apple M2 Chip Results:

- **Inference Speed:** ~21ms per image
- **Example Output:**
  - Confidence: 0.96, Class: person
  - Confidence: 0.89, Class: bottle
  - Speed: 2.3ms preprocess, 21.3ms inference, 9.6ms postprocess

### Key Takeaways:

- The Apple M2 chip significantly outperforms a standard CPU in inference speed, making it an excellent choice for real-time applications.
- Not only with NVIDIA's CUDA, but we can also achieve faster performance with the M2 chip.
- The implementation required minimal changes to the existing setup, making it incredibly easy to integrate.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- Streamlit
- Ultralytics
- YOLOv8 model
- Apple M2 chip (optional, for performance comparison)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/agustyawan-arif/yolov8-mps.git
   cd yoloyv8-mps
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

### Running the Application

1. Start the Flask API:

   ```sh
   python3 services/api.py
   ```

2. In a new terminal, start the Streamlit interface:

   ```sh
   python3 services/app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to access the Streamlit interface.
