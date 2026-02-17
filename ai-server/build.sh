#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Installing FFmpeg..."
mkdir -p bin

# Download static FFmpeg build
if [ ! -f bin/ffmpeg ]; then
    curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -o ffmpeg.tar.xz
    
    # Extract only ffmpeg and ffprobe, stripping the top-level directory
    # The structure is usually ffmpeg-x.x.x-amd64-static/ffmpeg
    tar -xf ffmpeg.tar.xz --strip-components=1 -C bin --wildcards '*/ffmpeg' '*/ffprobe'
    
    rm ffmpeg.tar.xz
    chmod +x bin/ffmpeg bin/ffprobe
    echo "FFmpeg installed in ./bin"
else
    echo "FFmpeg already exists in ./bin"
fi
