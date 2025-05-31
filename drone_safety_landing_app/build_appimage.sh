#!/bin/bash

APP=drone_safety_landing_app
VERSION=1.0

echo "🔧 Building $APP v$VERSION AppImage..."

mkdir -p AppDir/usr
cp -r core gui utils config models assets main.py requirements.txt AppDir/usr/

cat > AppDir/AppRun << EOF
#!/bin/bash
cd \$(dirname "\$0")/usr
python3 main.py
EOF

chmod +x AppDir/AppRun

cat > AppDir/$APP.desktop << EOF
[Desktop Entry]
Name=Drone Safety Landing App
Exec=AppRun
Icon=logo
Type=Application
Categories=Utility;
EOF

cp assets/logo.png AppDir/logo.png

appimagetool AppDir "${APP}-${VERSION}.AppImage"
