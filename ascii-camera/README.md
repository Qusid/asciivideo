# README.md

# ASCII Camera

This project is a Python application that converts the feed from a camera to ASCII art. It captures video frames from a camera and processes them to display as ASCII characters.

## Project Structure

```
ascii-camera
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── camera
│   │   ├── __init__.py
│   │   └── capture.py
│   └── ascii
│       ├── __init__.py
│       └── converter.py
├── tests
│   ├── __init__.py
│   ├── test_capture.py
│   └── test_converter.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd ascii-camera
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will start the camera feed and display the ASCII art in the terminal.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.