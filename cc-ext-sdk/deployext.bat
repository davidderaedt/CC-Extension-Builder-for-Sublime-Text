@echo off
set cepdir=CEP
set dest=%APPDATA%\Adobe\%cepdir%\extensions\%2
XCOPY "%1" %dest% /D /E /C /R /I /K /Y >nul
echo %dest%