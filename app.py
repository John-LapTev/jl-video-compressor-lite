import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, 
                             QProgressBar, QMessageBox, QLineEdit, QSlider, QFrame, QDesktopWidget)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QSize, QUrl
from PyQt5.QtGui import QDesktopServices

from video_compressor import VideoCompressor
from ui_components import create_slider_labels, create_info_frame, create_pro_version_link, create_developer_info
from styles import set_styles
from utils import format_size
from constants import WINDOW_TITLE, INITIAL_WINDOW_SIZE, EXPANDED_WINDOW_SIZE
from file_operations import select_input_file, select_output_directory

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = WINDOW_TITLE
        self.input_path = None
        self.output_dir = None
        self.original_file_size = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, *INITIAL_WINDOW_SIZE)
        set_styles(self)

        layout = QVBoxLayout()

        # File selection
        self.input_label = QLabel('Входной файл: Не выбран')
        layout.addWidget(self.input_label)
        self.input_button = QPushButton('Выбрать файл')
        self.input_button.clicked.connect(self.select_input)
        layout.addWidget(self.input_button)

        # Hidden section
        self.hidden_widget = QWidget()
        hidden_layout = QVBoxLayout()

        # Output directory
        self.output_dir_label = QLabel('Папка сохранения: Не выбрана')
        hidden_layout.addWidget(self.output_dir_label)
        self.output_dir_button = QPushButton('Изменить папку сохранения')
        self.output_dir_button.clicked.connect(self.select_output_dir)
        hidden_layout.addWidget(self.output_dir_button)

        # Output filename
        hidden_layout.addWidget(QLabel('Имя выходного файла:'))
        self.output_name_edit = QLineEdit()
        hidden_layout.addWidget(self.output_name_edit)

        # Quality slider
        hidden_layout.addWidget(QLabel('Баланс качества и сжатия (CRF):', objectName='sliderLabel'))
        self.quality_slider = QSlider(Qt.Horizontal)
        self.quality_slider.setMinimum(16)
        self.quality_slider.setMaximum(37)
        self.quality_slider.setValue(23)
        self.quality_slider.setTickPosition(QSlider.TicksBelow)
        self.quality_slider.setTickInterval(3)
        self.quality_slider.valueChanged.connect(self.update_quality_info)
        hidden_layout.addWidget(self.quality_slider)

        hidden_layout.addLayout(create_slider_labels())

        # Info frame
        self.info_frame = create_info_frame()
        hidden_layout.addWidget(self.info_frame)

        # Compress button
        self.compress_button = QPushButton('Сжать')
        self.compress_button.clicked.connect(self.compress_video)
        hidden_layout.addWidget(self.compress_button)

        # Progress bar
        self.progress_bar = QProgressBar()
        hidden_layout.addWidget(self.progress_bar)

        # Open folder button
        self.open_folder_button = QPushButton('Открыть папку', objectName="openFolderButton")
        self.open_folder_button.clicked.connect(self.open_output_folder)
        self.open_folder_button.setEnabled(False)
        hidden_layout.addWidget(self.open_folder_button)

        self.hidden_widget.setLayout(hidden_layout)
        layout.addWidget(self.hidden_widget)
        self.hidden_widget.hide()  # Скрываем виджет при инициализации

        # Pro version link
        layout.addWidget(create_pro_version_link())

        # Developer info
        layout.addLayout(create_developer_info())

        self.setLayout(layout)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def select_input(self):
        self.input_path = select_input_file()
        if self.input_path:
            self.input_label.setText(f'Входной файл: {os.path.basename(self.input_path)}')
            self.output_dir = os.path.dirname(self.input_path)
            self.output_dir_label.setText(f'Папка сохранения: {self.output_dir}')
            self.original_file_size = os.path.getsize(self.input_path)
            self.info_frame.findChild(QLabel, 'original_size_label').setText(f'Размер оригинала: {format_size(self.original_file_size)}')
            self.update_output_name()
            self.update_quality_info(self.quality_slider.value())
            
            self.animate_window_expansion()

    def select_output_dir(self):
        self.output_dir = select_output_directory()
        if self.output_dir:
            self.output_dir_label.setText(f'Папка сохранения: {self.output_dir}')

    def update_quality_info(self, value):
        if value < 20:
            quality = "Высокое качество"
        elif value < 27:
            quality = "Баланс"
        else:
            quality = "Сильное сжатие"
        self.info_frame.findChild(QLabel, 'quality_label').setText(f'Качество: {quality}')
        self.info_frame.findChild(QLabel, 'crf_label').setText(f'CRF: {value}')
        self.update_file_size_estimation(value)
        self.update_output_name()

    def update_file_size_estimation(self, crf):
        if self.original_file_size > 0:
            base_size_ratio = 0.5
            crf_factor = (23 - crf) / 35
            size_ratio = base_size_ratio + crf_factor
            
            if crf <= 18:
                size_ratio = min(size_ratio * 1.3, 0.95)
            elif crf >= 28:
                size_ratio = max(size_ratio * 0.7, 0.15)
            
            estimated_size = self.original_file_size * size_ratio
            self.info_frame.findChild(QLabel, 'file_size_label').setText(f'Примерный размер: {format_size(estimated_size)}')
        else:
            self.info_frame.findChild(QLabel, 'file_size_label').setText('Примерный размер: N/A')

    def update_output_name(self):
        if self.input_path:
            input_name = os.path.splitext(os.path.basename(self.input_path))[0]
            crf_value = self.quality_slider.value()
            self.output_name_edit.setText(f'CRF_{crf_value}_{input_name}.mp4')

    def animate_window_expansion(self):
        current_pos = self.pos()
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setStartValue(self.geometry())
        target_geometry = QRect(current_pos, QSize(*EXPANDED_WINDOW_SIZE))
        self.animation.setEndValue(target_geometry)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        
        self.hidden_widget.show()
        self.fade_in_animation = QPropertyAnimation(self.hidden_widget, b"windowOpacity")
        self.fade_in_animation.setDuration(300)
        self.fade_in_animation.setStartValue(0)
        self.fade_in_animation.setEndValue(1)
        self.fade_in_animation.setEasingCurve(QEasingCurve.InOutQuad)
        
        self.animation.start()
        self.fade_in_animation.start()

    def compress_video(self):
        if not self.input_path or not self.output_dir:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите входной файл и папку для сохранения.")
            return

        output_name = self.output_name_edit.text()
        if not output_name:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, введите имя выходного файла.")
            return

        output_path = os.path.join(self.output_dir, output_name)
        crf = self.quality_slider.value()

        self.compressor = VideoCompressor(self.input_path, output_path, crf)
        self.compressor.progress.connect(self.update_progress)
        self.compressor.finished.connect(self.compression_finished)
        self.compressor.error.connect(self.compression_error)
        self.compressor.start()

        self.compress_button.setEnabled(False)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def compression_finished(self):
        self.progress_bar.setValue(100)
        self.compress_button.setEnabled(True)
        self.open_folder_button.setEnabled(True)
        QMessageBox.information(self, "Успех", "Сжатие видео завершено успешно.")

    def compression_error(self, error_message):
        self.compress_button.setEnabled(True)
        QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при сжатии видео: {error_message}")

    def open_output_folder(self):
        if self.output_dir:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.output_dir))