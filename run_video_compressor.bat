@echo off

REM Set the project directory
set "PROJECT_DIR=%~dp0"

REM Create and activate virtual environment
if not exist "%PROJECT_DIR%venv" (
    python -m venv "%PROJECT_DIR%venv"
)
call "%PROJECT_DIR%venv\Scripts\activate.bat"

REM Upgrade pip
python -m pip install --upgrade pip

REM Install and upgrade required packages
pip install --upgrade PyQt5 pyinstaller

REM Create EXE file
pyinstaller --name=JLVideoCompressor --onefile --windowed ^
    --add-data "%PROJECT_DIR%app.py;." ^
    --add-data "%PROJECT_DIR%video_compressor.py;." ^
    --add-data "%PROJECT_DIR%ui_components.py;." ^
    --add-data "%PROJECT_DIR%styles.py;." ^
    --add-data "%PROJECT_DIR%utils.py;." ^
    --add-data "%PROJECT_DIR%constants.py;." ^
    --add-data "%PROJECT_DIR%file_operations.py;." ^
    --add-data "%PROJECT_DIR%ffmpeg.exe;." ^
    --add-data "%PROJECT_DIR%ffprobe.exe;." ^
    "%PROJECT_DIR%main.py"

REM Check if EXE file was created
if exist "%PROJECT_DIR%dist\JLVideoCompressor.exe" (
    echo EXE file created successfully.
    REM Run the program
    "%PROJECT_DIR%dist\JLVideoCompressor.exe"
) else (
    echo Failed to create EXE file.
)

REM Deactivate virtual environment
call "%PROJECT_DIR%venv\Scripts\deactivate.bat"

REM Keep the window open
pause