#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import glob
import time
import stat
import Image


def createDirThumbnails(pictureDir, thumbDir, size = (128,128) ):
    fileList = glob.glob(os.path.join(pictureDir, '*.jpg'))
    fileList = fileList + glob.glob(os.path.join(pictureDir, '*.JPG'))
    for file in fileList:
        st = os.stat(file)
        mode = st[stat.ST_MODE]
        if mode & stat.S_IWRITE: # file is readable
            if os.path.islink(file): # if it is a link, read the linked to file.
                file = os.readlink(file)
            baseName = os.path.basename(file)
            if not os.path.exists(thumbDir):
                os.makedirs(thumbDir)
        
            thumbName = os.path.join(thumbDir, baseName)
            if not os.path.exists(thumbName):
                im = Image.open(pictureDir + '/' + baseName)
                try:
                    im.thumbnail(size, Image.ANTIALIAS)
                except IOError:
                    raise IOError("Unexpected error for file " + baseName)
                
                im.save(thumbName, "JPEG")


def getThumbnail( filename, size = (128,128) ):
    '''Get a thumbnail image of filename'''
    
    im = Image.open(filename)
    im.thumbnail(size, Image.ANTIALIAS)
    newim = Image.new('RGB', size)
    x,y = im.size
    newim.paste(im, ((size[0]-x)/2, (size[1]-y)/2))
    return newim

