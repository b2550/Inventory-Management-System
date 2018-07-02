"""
Client Applet for Inventory Manager. Sends USB scanner data to server.
"""
import os
os.environ['QT_API'] = 'pyqt5'
import config
import logging
import logging.handlers
from appdirs import user_log_dir, user_config_dir, user_data_dir
import sys
from formlayout import fedit
import configparser
import argparse
import pync
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def initLogger():
    """
    Initialize the logger with file output to library/logs and stdout
    """
    global logger
    logger = logging.getLogger('InventoryManager')

    # Find log directory
    if not os.path.exists(config.LOG_DIR):
        os.makedirs(config.LOG_DIR)

    # Logger File Handler
    format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    logger.setLevel(config.LOG_DEBUG_LEVEL)
    handler = logging.handlers.RotatingFileHandler(os.path.join(config.LOG_DIR, 'InventoryManager.log'), maxBytes=20, backupCount=5)
    handler.setFormatter(format)
    logger.addHandler(handler)

    # stdout Logger Handler
    if init_args.quiet != True:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(config.CONSOLE_LOG_DEBUG_LEVEL)
        ch.setFormatter(format)
        logger.addHandler(ch)

def initLocalConfig():
    """
    Initialize local configuration file (not to be confused with the app configuration in config.py)
    """
    logger.info('Checking for config file')

    # Configuration object
    global localConfig
    localConfig = configparser.ConfigParser()

    # If config is found
    if os.path.isfile(config.CONFIG_FILE):
        logger.info('Found config file')

        # Load config from file
        localConfig.read(config.CONFIG_FILE)
    else:
        logger.info('Did not find config file. Creating one...')

        # Create config values
        localConfig['API'] = {'server' : '',
                              'api-key' : ''}

        # Save config values as file
        with open(config.CONFIG_FILE, 'w') as configfile:
            localConfig.write(configfile)
            logger.debug('Config file \"%s\" created successfully', config.CONFIG_FILE)

        # Prompt to edit config
        editPreferences(comment='<b>Welcome!</b> <br> <br> Please set URL and API key for the Inventory Manager server. <br> <br> You can get an API key by logging in as an admin on the Inventory Manager web interface and going to <b>Settings > API keys</b>. <br> <br> <i>(You can always do this later...)</i>')

def editPreferences(comment=''):
    """
    Edit local configuration through GUI
    """
    logger.info('Opening preferences')

    # Create preferences window
    pref_list = [('Server', localConfig.get('API', 'server')),
                 ('API Key', localConfig.get('API', 'api-key'))]

    # Display preferences window
    prefs = fedit(pref_list, title='Inventory Manager Preferences', comment=comment)

    logger.info('Closing preferences')
    logger.debug('Preferences data: %s', prefs)
    if prefs != None:
        localConfig['API'] = {'server' : prefs[0],
                              'api-key' : prefs[1]}
        with open(config.CONFIG_FILE, 'w') as configfile:
            localConfig.write(configfile)

def exitApp():
    """
    Exit the application
    """
    logger.info('Inventory Manager Stopping')
    sys.exit()

def initApp():
    """
    Create Qt5 tray icon
    """
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Create the icon
    icon = QIcon('icon.jpg')

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    preferences = QAction('Preferences')
    preferences.triggered.connect(editPreferences)
    menu.addAction(preferences)

    quit = QAction('Quit')
    quit.triggered.connect(exitApp)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    logger.info('Inventory Manager Started')

    #TODO: Here is when to attempt to connect to server
    pync.notify('Inventory Manager Started', title='Inventory Manager')

    app.exec_()

def initArguments():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Start the Inventory Manager client')
    parser.add_argument('--debug', '-d', help='Debug Mode', action='store_true')
    parser.add_argument('--collect', '-c', help='Collect all files in local directory', action='store_true')
    parser.add_argument('--quiet', '-q', help='Don\'t output log to command line', action='store_true')
    global init_args
    init_args = parser.parse_args()

    # Set app configuration from arguments
    if init_args.debug:
        config.debug = True
    if init_args.collect:
        config.collect = True

if __name__ == '__main__':
    # Check for OSX
    if sys.platform != 'darwin':
        raise Error('Platform Error: This software is only made to run on macOS')

    # Command line argument parser
    initArguments()

    # Start logger
    initLogger()

    logger.info('Inventory Manager Starting')

    if config.debug:
        logger.warning('INVENTORY MANAGER IS IN DEBUG MODE.')

    if config.collect:
        logger.warning('INVENTORY MANAGER IS IN COLLECT MODE. ALL LOCAL DATA WILL BE STORED IN CURRENT DIRECTORY.')

    # Initialize local configuration file (not to be confused with the app configuration in config.py)
    initLocalConfig()

    # Start the application
    initApp()
