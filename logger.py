import logging
import os


def get_logger(name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_name = f"{name}.log"
    file_path = str(os.path.join(current_path, file_name))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt='[%(asctime)s.%(msecs)03d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = logging.FileHandler(filename=file_path, mode='a', encoding='UTF-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
