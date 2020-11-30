#!/usr/bin/env python

import os
import shutil
import datetime
import readline    
from PIL import Image

print """
The following script captures all images, of type JPG and PNG, 
in the specified source path and copies them to folders sorted by year/month/day
"""

def main():
    default_dir = os.getcwd()
    srcdir = rlinput("Source Directory [Current]: ", default_dir)
    destdir = rlinput("Destination Directory [Current]: ", default_dir)

    for file in os.listdir(srcdir):
        supportedFormats = [".jpg",".png"]
        ext = os.path.splitext(file)[1]
        if ext.lower() not in supportedFormats:
            print "File Format of " + file + " not supported!"
            continue
        else:
            imagepath = srcdir + "/" + file
            imageDate = getDate(imagepath)

            if imageDate != None:

                year = imageDate.strftime('%Y')
                month = imageDate.strftime('%B')
                day = imageDate.strftime('%d')

                sortedImageDir = destdir + "/" + year + "/" + month + "/" + day + "/"
                if not os.path.exists(sortedImageDir):
                    print "The folder " + sortedImageDir + " was created..."
                    os.makedirs(sortedImageDir)
       
                shutil.copy2(imagepath, sortedImageDir + file)

def getDate(image):
    date = None
    i = Image.open(image)
    raw_date = i.getexif().get(36867)
    if raw_date != None:
        date = datetime.datetime.strptime(raw_date, '%Y:%m:%d %H:%M:%S')

    return date

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return raw_input(prompt)
   finally:
      readline.set_startup_hook()

if __name__ == '__main__':
    main()
