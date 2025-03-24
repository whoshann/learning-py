Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /k echo off & mouseevent /x 1000 /y 1000 & timeout /t 1"