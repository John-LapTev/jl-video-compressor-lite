from PyQt5.QtWidgets import QFileDialog
from constants import SUPPORTED_VIDEO_FORMATS

def select_input_file():
    """
    Открывает диалоговое окно для выбора входного видеофайла.
    """
    file_filter = "Видео файлы ({})".format(" ".join(SUPPORTED_VIDEO_FORMATS))
    file_path, _ = QFileDialog.getOpenFileName(None, "Выберите входное видео", "", file_filter)
    return file_path if file_path else None

def select_output_directory():
    """
    Открывает диалоговое окно для выбора директории сохранения.
    """
    directory = QFileDialog.getExistingDirectory(None, "Выберите папку для сохранения")
    return directory if directory else None

# Здесь можно добавить другие функции для работы с файлами по мере необходимости