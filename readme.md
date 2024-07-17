# JL Video Compressor Lite

JL Video Compressor Lite - это простое в использовании приложение для сжатия видеофайлов, разработанное на Python с использованием PyQt5 для графического интерфейса и FFmpeg для обработки видео.

## Особенности

- Простой и интуитивно понятный пользовательский интерфейс
- Настраиваемый уровень сжатия с помощью слайдера CRF
- Оценка размера сжатого файла в реальном времени
- Отображение прогресса сжатия
- Поддержка популярных видеоформатов (MP4, AVI, MOV)

## Требования

- Python 3.7+
- PyQt5
- FFmpeg

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/John-LapTev/jl-video-compressor-lite.git
   ```

2. Перейдите в директорию проекта:
   ```
   cd jl-video-compressor-lite
   ```

3. Установите необходимые зависимости:
   ```
   pip install PyQt5
   ```

4. Установка FFmpeg:
   - Скачайте FFmpeg с официального сайта: https://ffmpeg.org/download.html
   - Распакуйте архив
   - Поместите файлы ffmpeg.exe и ffprobe.exe в корневую папку проекта

   Примечание: файлы ffmpeg.exe и ffprobe.exe не включены в репозиторий из-за ограничений GitHub на размер файлов.

## Запуск приложения

1. Запустите файл `main.py`:
   ```
   python main.py
   ```

2. Или используйте батч-файл `run_video_compressor.bat` для Windows:
   ```
   run_video_compressor.bat
   ```

## Использование

1. Нажмите кнопку "Выбрать файл" и выберите видеофайл для сжатия.
2. Настройте уровень сжатия с помощью слайдера CRF.
3. При желании измените имя выходного файла и папку для сохранения.
4. Нажмите кнопку "Сжать" для начала процесса сжатия.
5. После завершения сжатия вы можете открыть папку с результатом.

## Разработчик

- [John LapTev](https://t.me/John_LapTev)
- [Boosty](https://boosty.to/jlsd)
- [YouTube](https://youtube.com/@cheesez_crazy)

## Лицензия

Этот проект лицензирован под лицензией MIT - см. файл [LICENSE](LICENSE) для подробностей.
