from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt

def create_slider_labels():
    slider_labels_layout = QHBoxLayout()
    slider_labels_layout.addWidget(QLabel('Высокое качество'))
    slider_labels_layout.addStretch()
    slider_labels_layout.addWidget(QLabel('Баланс'))
    slider_labels_layout.addStretch()
    slider_labels_layout.addWidget(QLabel('Сильное сжатие'))
    return slider_labels_layout

def create_info_frame():
    info_frame = QFrame(objectName="infoFrame")
    info_layout = QVBoxLayout()
    
    original_size_label = QLabel('Размер оригинала: N/A')
    original_size_label.setObjectName('original_size_label')
    original_size_label.setProperty('class', 'title')
    info_layout.addWidget(original_size_label)
    
    quality_label = QLabel('Качество: Баланс')
    quality_label.setObjectName('quality_label')
    quality_label.setProperty('class', 'title')
    info_layout.addWidget(quality_label)
    
    crf_label = QLabel('CRF: 23')
    crf_label.setObjectName('crf_label')
    crf_label.setProperty('class', 'value')
    info_layout.addWidget(crf_label)
    
    file_size_label = QLabel('Примерный размер: N/A')
    file_size_label.setObjectName('file_size_label')
    file_size_label.setProperty('class', 'value')
    info_layout.addWidget(file_size_label)
    
    info_frame.setLayout(info_layout)
    return info_frame

def create_pro_version_link():
    pro_link = QLabel('<a href="https://boosty.to/jlsd">Купить "JL Video Compressor PRO"</a>')
    pro_link.setOpenExternalLinks(True)
    pro_link.setObjectName("proVersionLink")
    return pro_link

def create_developer_info():
    dev_layout = QHBoxLayout()
    dev_layout.addWidget(QLabel('Разработчик:'))
    john_laptev_link = QLabel('<a href="https://t.me/John_LapTev">John LapTev</a>')
    john_laptev_link.setOpenExternalLinks(True)
    dev_layout.addWidget(john_laptev_link)
    dev_layout.addWidget(QLabel('|'))
    boosty_link = QLabel('<a href="https://boosty.to/jlsd">Boosty</a>')
    boosty_link.setOpenExternalLinks(True)
    dev_layout.addWidget(boosty_link)
    dev_layout.addWidget(QLabel('|'))
    youtube_link = QLabel('<a href="https://youtube.com/@cheesez_crazy">YouTube</a>')
    youtube_link.setOpenExternalLinks(True)
    dev_layout.addWidget(youtube_link)
    dev_layout.addStretch()
    return dev_layout