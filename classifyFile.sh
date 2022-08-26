#!/bin/bash

name =$(whoami)

echo "Hello $name, Classifying Files Start Now!"


[ -d Pictures ] && echo "Directory Exist" || mkdir ./Pictures
find . -name "*.png" -exec mv "{}" ./Pictures \;
find . -name "*.jpg" -exec mv "{}" ./Pictures \;
find . -name "*.jpeg" -exec mv "{}" ./Pictures \;
find . -name "*.svg" -exec mv "{}" ./Pictures \;

[ -d Videos ] && echo "Directory Exist" || mkdir ./Videos
find . -name "*.gif" -exec mv "{}" ./Videos \; 
find . -name "*.mkv" -exec mv "{}" ./Videos \;
find . -name "*.mp4" -exec mv "{}" ./Videos \;
find . -name "*.MOV" -exec mv "{}" ./Videos \;

[ -d Documents ] && echo "Directory Exist" || mkdir ./Documents
find . -name "*.pdf" -exec mv "{}" ./Documents \;
find . -name "*.html" -exec mv "{}" ./Documents \;
find . -name "*.txt" -exec mv "{}" ./Documents \;

[ -d File  ] && echo "Directory Exist" || mkdir ./File
find . -name "*.psd" -exec mv "{}" ./File \;
find . -name "*.cdr" -exec mv "{}" ./File \;

[ -d Data ] && echo "Directory Exist" || mkdir ./Data
find . -name "*.xlsm" -exec mv "{}" ./Data \;
find . -name "*.xlsx" -exec mv "{}" ./Data \;
find . -name "*.xls" -exec mv "{}" ./Data \;
find . -name "*.pptx" -exec mv "{}" ./Data \;
find . -name "*.docx" -exec mv "{}" ./Data \;
find . -name "*.csv" -exec mv "{}" ./Data \;

[ -d Fonts ] && echo "Directory Exist" || mkdir ./Fonts
find . -name "*.ttf" -exec mv "{}" ./Fonts \;

[ -d Archieves ] && echo "Directory Exist" || mkdir ./Archieves
find . -name "*.zip" -exec mv "{}" ./Archieves \;

[ -d Application ] && echo "Directory Exist" || mkdir ./Application
find . -name "*.pkg" -exec mv "{}" ./Application \;
find . -name "*.exe" -exec mv "{}" ./Application \;
find . -name "*.dmg" -exec mv "{}" ./Application \;

