@echo off
IF "%1"=="ps" (
	"%PROGRAMFILES%\Adobe\Adobe Photoshop CC (64 Bit)\Photoshop.exe" %2
) ELSE IF "%1"=="ai" (
	"%PROGRAMFILES%\Adobe\Adobe Illustrator CC (64 Bit)\Support Files\Contents\Windows\Illustrator.exe" %2
) ELSE IF "%1"=="ae" (
	"%PROGRAMFILES%\Adobe\Adobe After Effects CC\Support Files\AfterFx.exe" -r %2
) ELSE (
	echo "Unrecognized adobe program"
)

