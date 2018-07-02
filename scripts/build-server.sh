#!/bin/sh

# Installs virtual enviroment and runs tests

echo "Building server"
echo "Initializing pipenv for server"
cd server
pipenv install --python 3
