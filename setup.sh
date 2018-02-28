#!/bin/bash
# Installation script for package dependencies

# sudo visudo
###### pip3
sudo pip3 install librosa
sudo pip3 install numpy
sudo pip3 install scipy
sudo pip3 install matplotlib
sudo pip3 install --upgrade google-cloud-vision
sudo pip3 install opencv-python
sudo pip3 install watson-developer-cloud
sudo export GOOGLE_APPLICATION_CREDENTIALS=$HOME/logmein-capstone_2017-18/backend/Video/google_api_credentials.json


# ffmpeg
sudo apt-get -qq ffmpeg


###### curl
# this gets the macOS 7z file
# curl -o ffmpeg.7z https://evermeet.cx/ffmpeg/ffmpeg-90169-gf4709f1b7b.7z


# this is for Debian
# curl -o ffmpeg.tar.xz http://security.debian.org/debian-security/pool/updates/main/f/ffmpeg/ffmpeg_3.2.10.orig.tar.xz

# unzip
# ./configure

# $USER ALL=NOPASSWD: /usr/bin/apt-get install
