@echo off
set bookmark_name=%1



if not exist "%USERPROFILE%\marlin" (
    md  %USERPROFILE%\marlin
    echo creada carpeta de marlin
)

if [%bookmark_name%]==[] goto :HELP

if exist "%USERPROFILE%\marlin\%bookmark_name%" (
    set /p bname=<%USERPROFILE%\marlin\%bookmark_name%
    cd %bname%
    goto :END
) else (
    echo no existe el archivo %bookmark_name%
    goto :END
)

:HELP
python marlin_help.py

:END