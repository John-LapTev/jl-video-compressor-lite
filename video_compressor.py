import subprocess
import re
from PyQt5.QtCore import QThread, pyqtSignal

class VideoCompressor(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, input_path, output_path, crf):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path
        self.crf = crf

    def run(self):
        try:
            result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', self.input_path], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            duration = float(result.stdout)

            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            process = subprocess.Popen(['ffmpeg', '-i', self.input_path, '-c:v', 'libx264', '-preset', 'medium', 
                                        '-crf', str(self.crf), '-c:a', 'aac', '-b:a', '128k', self.output_path], 
                                       stderr=subprocess.PIPE, universal_newlines=True, startupinfo=startupinfo)

            for line in process.stderr:
                match = re.search(r'time=(\d{2}):(\d{2}):(\d{2})\.\d+', line)
                if match:
                    hours, minutes, seconds = map(int, match.groups())
                    time_processed = hours * 3600 + minutes * 60 + seconds
                    progress = min(int(time_processed / duration * 100), 100)
                    self.progress.emit(progress)

            process.wait()

            if process.returncode != 0:
                raise Exception("FFmpeg process failed")

            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))