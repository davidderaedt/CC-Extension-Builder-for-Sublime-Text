@echo off
IF "%1"=="ps" (
	"%PROGRAMFILES%\Adobe\Adobe Photoshop CC 2014\Photoshop.exe" %2
) ELSE IF "%1"=="ai" (
	"%PROGRAMFILES%\Adobe\Adobe Illustrator CC 2014\Support Files\Contents\Windows\Illustrator.exe" %2
) ELSE IF "%1"=="ae" (
	"%PROGRAMFILES%\Adobe\Adobe After Effects CC 2014\Support Files\AfterFx.exe" -r %2
) ELSE (
	echo "Unrecognized adobe program"
)

