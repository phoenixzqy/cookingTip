#!/bin/bash

appname=cookingTip
entry=main.py
# build app
pyinstaller --clean -F -n $appname $entry
# copy static files
cp static ./dist/static