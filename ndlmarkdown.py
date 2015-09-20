
#!/usr/bin/env python

# HTML utilities

import os
import sys
import re
import shutil
import time
import string
import glob
import datetime
import httplib

def getReference(keyName):
    requestURL = 'ml.sheffield.ac.uk'
    requestString = '/~neil/cgi-bin/publications/bibpage.cgi?keyName=' + keyName + '&header=0&printAbstract=1'
    print "Getting publication " + keyName 
    print "Using " + requestURL + requestString
    h = httplib.HTTP(requestURL)
    h.putrequest('GET', requestString)
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        print "... succesful."
    else:
        print "Error " + str(errcode) + ", " + errmsg
    f = h.getfile()
    lines = f.read()
    f.close()
    return lines
    
def writeToFile(file, string, style = '', title='', header='', footer='', navigation=''):
    header = '<html>\n' + header
    if len(title)>0:
        header += "<head>\n  <title>" + title + "</title>\n</head>\n"
    header += "<body>\n\n"
    header += navigation
    header += '<section id="content" class="three-col">\n<div id="inner">'
    string = header + string 
    string += "<p>This document last modified <!--#flastmod file=\"" + file + "\" --></p>"
    string += "\n</div>\n</section>"
    if len(footer)>0:
        string += footer
    string += "\n</html>"
    fileHandle = open(file, 'w')
    fileHandle.write(string)
    fileHandle.close()

