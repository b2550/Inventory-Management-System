#!/bin/sh

# Installs virtual enviroment, builds app with py2app, and runs tests

echo "Building Client"
echo "Initializing pipenv for client"

cd client
pipenv install

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
  echo "Building client with py2app"
  pipenv run python setup.py py2app
fi
