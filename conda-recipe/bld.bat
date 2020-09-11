"%PYTHON%" setup.py install --single-version-externally-managed --record=%TEMP%\record.txt --version "%APPVEYOR_BUILD_VERSION%"
if errorlevel 1 exit 1
