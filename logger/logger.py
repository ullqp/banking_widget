import logging

utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="logs/utils.log", mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)

masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename='logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
