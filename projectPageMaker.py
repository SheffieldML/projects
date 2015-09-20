#!/usr/bin/env python

# File for publishing project pages to the web.

import os
import sys
import re
import shutil
import time
import string
import httplib
import posix
import yaml

sys.path.append(os.path.join(posix.environ['HOME'], 'public_html', 'cgi-bin'))
import ndltext
import ndlfile
import ndlhtml


homeDir = os.getenv('HOME')

#projectHeader.txt contains the pages' headers

sheffieldPersonBase = 'http://www.dcs.sheffield.ac.uk/cgi-bin/makeperson?'
sheffieldBase = 'http://ml.sheffield.ac.uk/'
year = time.strftime('%Y')
timeStamp = time.strftime('%A %d %b %Y at %H:%M')
f = open('project.yml', 'r')
project = yaml.load(f)

overview=''
fileHandle = open('overview.md', 'r');
fileLines = fileHandle.readlines()
fileHandle.close()
for line in fileLines:
    overview += line

outputString="# " + project['shortname'] + " Project\n\n"
outputString += "## Overview"
outputString+= "\n\n" + overview


if len(project['sponsors'])>0:
    outputString += "The project is sponsored by "
    for i, sponsor in enumerate(project['sponsors']):
        outputString += "[" + sponsor['name'] + " Project Ref " + str(sponsor['ref']) + "](" + sponsor['url'] + ")"
        if len(project['sponsors'])>1:
            if i==len(project['sponsors'])-1:
                outputString += ", "
            else:
                outputString += " and "
    if len(project['collaborators'])>0:
        outputString += " and is a collaboration with "
    else:
        outputString += ".\n\n" 
       
else:
    if len(project['collaborators'])>0:
        outputString += "The project is a collaboration with "

if len(project['collaborators'])>0:
    for i, collaborator in enumerate(project['collaborators']):
        outputString += "[" + collaborator['name'] + "](" + collaborator['url'] + ") of " + collaborator['institute']
        if len(project['collaborators'])>1:
            if i==len(project['collaborators'])-2:
                outputString += " and "
            elif i==len(project['collaborators'])-1:
                outputString += "."
            else:
                outputString += ", "
        else:
            outputString += ".\n\n"

if len(project['personnel'])>0:
    outputString+= "\n\n<a name=\"personnel\"></a>\n\n## Personnel from ML@SITraN\n\n"
    for person in project['personnel']:
        outputString += "- [" + person['name'] + "](" + person['url'] + ") " + person['role'] + "\n\n"

    outputString += "\n\n"

# Give information about software.
if len(project['software'])>1:
    outputString+= "<a name=\"software\"></a>\n\n## Software\n\n"
    outputString+= "The following software has been made available either wholly or partly as a result of work on this project:\n\n"
    for i, software in enumerate(project['software']):
        if software['url']=='local':
            outputString += "- [" + software['name'] + "](http://inverseprobability.com/" + software['name'] + ") " + software['tagline'] + "\n\n"
        elif software['url']=='SheffieldML':
            outputString += "- Github: [" + software['name'] + "](https://github.com/SheffieldML/" + software['name'] + ") " + software['tagline'] + "\n\n"
        else:
            outputString += "- [" + software['name'] + "](" + software['url'] + ") " + software['tagline'] + "\n\n"



# Give information about publications
if len(project['publications'])>0:
    outputString+="<a name=\"publications\"></a>\n\n## Publications\n\n"
for key in project['publications']:
    if key == 'conference':
        outputString+="The following conference publications were made associated with this project.\n\n"
    elif key == 'chapters':
        outputString+="The following edited chapters were published as part of this project.\n\n"
    elif key == 'journal':
        outputString+="The journal papers were published as part of this project.\n\n"
    elif key == 'books':
        outputString+="The following books were published as part of this project.\n\n"
    elif key == 'patents':
        outputString+="The patents were applied for as part of this project.\n\n"

    elif key == 'related':
        outputString+="The following publications have provided background to our work in this project.\n\n"

    for publicationkey in project['publications'][key]:
        outputString += ndlhtml.getMdReference(publicationkey)
        outputString += '\n\n'




ndlhtml.mdWriteToFile('index.md', outputString, '', project['shortname'], '', '', '')

