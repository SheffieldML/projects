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

sys.path.append(os.path.join(posix.environ['HOME'], 'public_html', 'cgi-bin'))
import ndltext
import ndlfile
import ndlhtml


homeDir = os.getenv('HOME')

#projectHeader.txt contains the pages' headers
fileNameBase = os.path.join(homeDir, 'SheffieldML', 'projects');
projectHeader = ndlfile.readTxtFile('projectHeader.txt', fileNameBase)
#projectFooter.txt contains the pages' footers
projectFooter = ndlfile.readTxtFile('projectFooter.txt', fileNameBase)
#projectStyle.txt contains the pages' style
projectStyle = ndlfile.readTxtFile('projectStyle.txt', fileNameBase)
# projectNavigation contains navigation bar.
projectNavigation = ndlfile.readTxtFile('projectNavigation.txt', fileNameBase)

# arguments PROJECTNAME
sheffieldPersonBase = 'http://www.dcs.sheffield.ac.uk/cgi-bin/makeperson?'
sheffieldBase = 'http://ml.sheffield.ac.uk/'
if len(sys.argv) < 2:
    raise "There should be an input argument (project name)."
year = time.strftime('%Y')
timeStamp = time.strftime('%A %d %b %Y at %H:%M')
projectName = sys.argv[1];
lowerProject = projectName.lower();

# personnel.txt contains staff/students information
personnelDetails = ndlfile.extractFileDetails('personnel.txt')
# collaborator.txt contains collaborator information
collaboratorDetails = ndlfile.extractFileDetails('collaborators.txt')
# software.txt contains software information.
softwareDetails = ndlfile.extractFileDetails('software.txt')
# title.txt contains the title of the project.
titleDetails = ndlfile.extractFileDetails('title.txt')
# sponsor.txt contains details of the sponsor.
sponsorDetails = ndlfile.extractFileDetails('sponsors.txt')
# publication.txt contains details of the publications.
publicationDetails = ndlfile.extractFileDetails('publications.txt')

overview=''
fileHandle = open('overview.md', 'r');
fileLines = fileHandle.readlines()
fileHandle.close()
for line in fileLines:
    overview += line

outputString="# " + titleDetails[0][1] + "\n\n"
outputString += "## Overview"
outputString+= "\n\n" + overview


if len(sponsorDetails)>0:
    outputString += "The project is sponsored by "
    for i in range(len(sponsorDetails)):
        outputString += "[" + sponsorDetails[i][0] + "](" + sponsorDetails[i][1] + ")"
        if len(sponsorDetails)>1:
            if i==len(sponsorDetails)-1:
                outputString += ", "
            else:
                outputString += " and "
    if len(collaboratorDetails)>0:
        outputString += " and is a collaboration with "
    else:
        outputString += ".\n\n" 
       
else:
    if len(collaboratorDetails)>0:
        outputString += "The project is a collaboration with "

if len(collaboratorDetails)>0:
    for i in range(len(collaboratorDetails)):
        outputString += "[" + collaboratorDetails[i][0] + "](" + collaboratorDetails[i][2] + ") of " + collaboratorDetails[i][1]
        if len(collaboratorDetails)>1:
            if i==len(collaboratorDetails)-2:
                outputString += " and "
            elif i==len(collaboratorDetails)-1:
                outputString += "."
            else:
                outputString += ", "
        else:
            outputString += ". \n\n"

if len(personnelDetails)>0:
    outputString+= "<a name=\"personnel\"></a>## Personnel from ML@SITraN\n\n"
    for i in range(len(personnelDetails)):
        outputString += "- [" + personnelDetails[i][0] + "](" + sheffieldPersonBase + personnelDetails[i][2] + "), " + personnelDetails[i][1] + "\n\n"

    outputString += "</table>\n\n"

# Give information about software.
if len(softwareDetails)>1:
    outputString+= "<a name=\"software\"></a><h2>Software</h2>\n\n"
    outputString+= "<p>The following software has been made available either wholly or partly as a result of work on this project:"
    for i in range(len(softwareDetails)):
        if softwareDetails[i][0]=='local':
            outputString += "- [" + softwareDetails[i][2] + "](http://inverseprobability.com/" + softwareDetails[i][1] + ")\n\n"
        elif softwareDetails[i][0]=='SheffieldML':
            outputString += "- Github: [" + softwareDetails[i][2] + "](https://github.com/SheffieldML/" + softwareDetails[i][1] + ")\n\n"
        else:
            outputString += "- [" + softwareDetails[i][2] + "](" + softwareDetails[i][1] + ")\n\n"



# Give information about publications
if len(publicationDetails)>0:
    outputString+="<a name=\"publications\"></a>## Publications\n\n"
    outputString+="The following publications have provided background to our work in this project."
    for i in range(len(publicationDetails)):
        for j in range(len(publicationDetails[i])):
            if j == 0:
                outputString += "### " + publicationDetails[i][0] + "\n\n"
            else:            
                outputString += ndlhtml.getReference(publicationDetails[i][j])
                outputString += '\n\n'

# Now create a web page
publishBase=os.path.expanduser(os.path.join("~", "public_html", "projects", lowerProject));

if not os.path.exists(publishBase):
    os.mkdir(publishBase)



ndlhtml.mdWriteToFile('index.md', outputString, projectStyle, titleDetails[0][0], projectHeader, projectFooter, projectNavigation)

shutil.copyfile('index.md', os.path.join(publishBase, 'index.md'))
