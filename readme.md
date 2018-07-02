# Inventory Manager
A solution for rental shops to keep track of checked out equipment through barcodes (scanner client is currently macOS-only)

# How to run (development)

1. Use pipenv to install required packages and their dependancies

`pipenv install`

2. Enter pipenv shell

`pipenv shell`

3. Run `client/app.py` and/or `server/app.py`

# Client
```
usage: app.py [-h] [--debug] [--collect] [--quiet]

Start the Inventory Manager client

optional arguments:
  -h, --help     show this help message and exit
  --debug, -d    Debug Mode
  --collect, -c  Collect all files in local directory
  --quiet, -q    Don't output log to command line
```

The client is made into a .app with [py2app](http://py2app.readthedocs.io/en/latest/)
