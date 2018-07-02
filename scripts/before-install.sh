#!/bin/sh

# Installs virtual enviroment and runs tests

echo "Running pre-install script"
cd client
if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
  brew update
  brew upgrade python
fi
