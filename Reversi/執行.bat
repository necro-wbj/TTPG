@echo off
:::::::::::::::::::::::::::::::::½Ð¨DÅv­­::::::::::::::::::::::::::::::::::::::::::::::::::
REM :init
REM setlocal DisableDelayedExpansion
REM set "batchPath=%~0"
REM for %%k in (%0) do set batchName=%%~nk
REM set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
REM setlocal EnableDelayedExpansion
REM :checkPrivileges
REM NET FILE 1>NUL 2>NUL
REM if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )
REM :getPrivileges
REM if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
REM ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
REM ECHO args = "ELEV " >> "%vbsGetPrivileges%"
REM ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
REM ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
REM ECHO Next >> "%vbsGetPrivileges%"
REM ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
REM "%SystemRoot%\System32\WScript.exe" "%vbsGetPrivileges%" %*
REM exit /B
REM :gotPrivileges
REM setlocal & pushd .
REM cd /d %~dp0
REM if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
python Game.py
pause