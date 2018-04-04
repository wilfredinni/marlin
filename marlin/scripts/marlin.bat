@ECHO OFF
set bookmark=%1
if [%bookmark%]==[] goto :none
if %bookmark%==do-pack goto :do-pack
if %bookmark%==desktop goto :desktop
if %bookmark%==uselessbot goto :uselessbot
if %bookmark%==marlin goto :marlin
if %bookmark%==root goto :root
if %bookmark%==projects goto :projects
if %bookmark%==carlos goto :carlos
:none
echo hola mundo
exit /b 0
:do-pack
cd c:\Dropbox\Dropbox\projects\python\do-pack
exit /b 0
:desktop
cd c:\Users\carlo\Desktop
exit /b 0
:uselessbot
cd c:\Dropbox\Dropbox\projects\python\retwiBot
exit /b 0
:marlin
cd C:\Dropbox\Dropbox\projects\python\marlin
exit /b 0
:root
cd c:\
exit /b 0
:projects
cd c:\Dropbox\Dropbox\projects\python
exit /b 0
:carlos
cd c:\Users\carlo
exit /b 0
