#!/bin/sh
rm -r dist

pyinstaller --onedir --console --hidden-import "encodings" --name "Remote Antivirus" ../src/main.py
pyinstaller --onefile --console --hidden-import "encodings" --name "Remote Antivirus (One-File)" ../src/main.py

rm -r build
rm *.spec
