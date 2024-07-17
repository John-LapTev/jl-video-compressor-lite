def set_styles(app):
    app.setStyleSheet("""
        QWidget {
            background-color: #f0f0f0;
            font-family: Arial;
        }
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton#openFolderButton {
            background-color: #008CBA;
        }
        QPushButton#openFolderButton:hover {
            background-color: #007B9A;
        }
        QLineEdit {
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            background-color: white;
        }
        QLabel {
            font-size: 14px;
        }
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #4CAF50;
        }
        #infoFrame {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        #infoFrame QLabel {
            background-color: #f8f8f8;
            border-radius: 5px;
            padding: 8px;
            margin-bottom: 5px;
        }
        #infoFrame QLabel[class="title"] {
            font-weight: bold;
            color: #333;
        }
        #infoFrame QLabel[class="value"] {
            color: #0066cc;
        }
        #sliderLabel {
            font-weight: bold;
            margin-top: 10px;
        }
        #proVersionLink {
            font-size: 12px;
            color: #666;
        }
    """)