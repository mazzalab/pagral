SET VERSION="1.1.1"
"%PYTHON%" setup.py install --single-version-externally-managed --record=%TEMP%\record.txt --bver %APPVEYOR_BUILD_VERSION%
if errorlevel 1 exit 1
