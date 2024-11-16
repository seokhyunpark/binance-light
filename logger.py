import logging
import os


class Logger:
    def __init__(self, name):
        self.name = name
        self.logger = None
        self._set_logger()

    def _set_logger(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = f"{self.name}.log"
        file_path = str(os.path.join(current_path, file_name))

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d] %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler = logging.FileHandler(filename=file_path, mode='a', encoding='UTF-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
