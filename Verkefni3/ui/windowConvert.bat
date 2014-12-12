@echo off

echo Converting window to python file

C:\Python34\Lib\site-packages\PyQt4\pyuic4 window.ui >> window.py

pause
cmd.exe