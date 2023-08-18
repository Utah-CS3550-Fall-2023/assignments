#!/bin/sh
set -e +x

if ! nc -z localhost 8000; then
    echo "No server running; please start the server and try again"
    exit 1
fi
/Applications/Firefox.app/Contents/MacOS/firefox \
    --headless --window-size 700,600 --screenshot "$PWD/$2" "http://localhost:8000/$1"
