[![GitHub license](https://img.shields.io/github/license/b2550/Inventory-Manager.svg?style=for-the-badge)](https://github.com/b2550/Inventory-Manager/blob/master/LICENSE)
[![Travis](https://img.shields.io/travis/b2550/Inventory-Manager.svg?style=for-the-badge)](https://travis-ci.org/b2550/Inventory-Manager)


# Inventory Manager
A solution for rental shops to keep track of checked out equipment through barcodes (scanner client is currently macOS-only)

# How to run (development)

1. Use pipenv to install required packages and their dependancies

`pipenv install`

2. Enter pipenv shell

`pipenv shell`

3. Run `client/__init__.py` and/or `server/__init__.py`

# Client
```
usage: __init__.py [-h] [--debug] [--collect] [--quiet]

Start the Inventory Manager client

optional arguments:
  -h, --help     show this help message and exit
  --debug, -d    Debug Mode
  --collect, -c  Collect all files in local directory
  --quiet, -q    Don't output log to command line
```

The client is made into a .app with [py2app](http://py2app.readthedocs.io/en/latest/)
