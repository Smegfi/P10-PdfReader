SET CurrentDir=%~dp0
xcopy "%CurrentDir%\poppler-0.68.0" "C:\Program Files\poppler-0.68.0" /E /C /I /Q
set PATH=%PATH%;C:\Program Files\poppler-0.68.0\bin

Pause