# JL Video Compressor Lite

JL Video Compressor Lite is a user-friendly application for compressing video files, developed in Python using PyQt5 for the graphical interface and FFmpeg for video processing.

## Features

- Simple and intuitive user interface
- Adjustable compression level using CRF slider
- Real-time estimation of compressed file size
- Display of compression progress
- Support for popular video formats (MP4, AVI, MOV)

## Requirements

- Python 3.7+
- PyQt5
- FFmpeg

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/John-LapTev/jl-video-compressor-lite.git
   ```

2. Navigate to the project directory:
   ```
   cd jl-video-compressor-lite
   ```

3. Install the required dependencies:
   ```
   pip install PyQt5
   ```

4. Install FFmpeg:
   - Download FFmpeg from the official website: https://ffmpeg.org/download.html
   - Extract the archive
   - Place the ffmpeg.exe and ffprobe.exe files in the root folder of the project

   Note: ffmpeg.exe and ffprobe.exe files are not included in the repository due to GitHub file size restrictions.

## Running the Application

1. Run the `main.py` file:
   ```
   python main.py
   ```

2. Or use the `run_video_compressor.bat` batch file for Windows:
   ```
   run_video_compressor.bat
   ```

## Usage

1. Click the "Select File" button and choose a video file to compress.
2. Adjust the compression level using the CRF slider.
3. Optionally, change the output file name and save folder.
4. Click the "Compress" button to start the compression process.
5. After compression is complete, you can open the folder with the result.

## Project Structure

- `main.py`: Main file to run the application
- `app.py`: Contains the App class, which represents the main application window
- `video_compressor.py`: Contains the VideoCompressor class for performing video compression
- `ui_components.py`: Functions for creating user interface components
- `styles.py`: Defines styles for user interface elements
- `utils.py`: Helper functions
- `constants.py`: Stores constants and configuration parameters
- `file_operations.py`: Functions for working with files and directories

## Developer

- [John LapTev](https://t.me/John_LapTev)
- [Boosty](https://boosty.to/jlsd)
- [YouTube](https://youtube.com/@cheesez_crazy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
