#!/bin/bash

cd /tmp
curl -LO https://raw.githubusercontent.com/tmxs/ImageSorter/master/ImageSorter.py
mv /tmp/ImageSorter.py ~/.local/bin/imagesorter
chmod +x ~/.local/bin/imagesorter
