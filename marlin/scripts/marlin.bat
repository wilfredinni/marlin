@echo off
set bookmark_name=%1

if not exist "%USERPROFILE%\.marlin" (
    goto :MDMARLIN
)

if [%bookmark_name%]==[] goto :HELP

if exist "%USERPROFILE%\.marlin\%bookmark_name%" (
    set /p bname=<"%USERPROFILE%\.marlin\%bookmark_name%"
    goto :CD
) else (
    echo Bookmark does not exists: %bookmark_name%
    goto :END
)
:MDMARLIN
md %USERPROFILE%\.marlin
goto :HELP

:HELP
marlin_help
exit /b 0

:CD
cd %bname%
exit /b 0

:END
