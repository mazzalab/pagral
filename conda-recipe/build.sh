#!/bin/sh
$PYTHON setup.py install --single-version-externally-managed --record=$RECIPE_DIR/record.txt --version "%APPVEYOR_BUILD_VERSION%"
