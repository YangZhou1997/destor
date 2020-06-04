# !/bin/bash
mkdir -p ~/dataset/
mkdir -p ~/dataset/fslhomes/
mkdir -p ~/dataset/macos/

cd ~/dataset/fslhomes/ && wget --random-wait -r -np -e robots=off -U -R "index.html*" -c http://tracer.filesystems.org/traces/fslhomes/2012/
cd ~/dataset/macos/ && wget --random-wait -r -np -e robots=off -U -R "index.html*" -c http://tracer.filesystems.org/traces/macos/2012/
