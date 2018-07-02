import logging
import os
from appdirs import user_log_dir, user_config_dir, user_data_dir

debug = False
collect = False

if collect:
    CONFIG_DIR = os.getcwd()
    CONFIG_FILE = os.path.join(os.getcwd(), 'config.ini')
    LOG_DIR = os.getcwd()
    DATA_DIR = os.getcwd()
    CONSOLE_LOG_DEBUG_LEVEL = logging.DEBUG
    LOG_DEBUG_LEVEL = logging.DEBUG
else:
    CONFIG_DIR = user_config_dir('Inventory Manager', 'TIMARA')
    CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.ini')
    LOG_DIR = user_log_dir('Inventory Manager', 'TIMARA')
    DATA_DIR = user_log_dir('Inventory Manager', 'TIMARA')
    CONSOLE_LOG_DEBUG_LEVEL = logging.INFO
    LOG_DEBUG_LEVEL = logging.INFO
