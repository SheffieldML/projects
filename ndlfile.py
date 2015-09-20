#!/usr/bin/env python

# Text utilities

import os
import sys
import re
import shutil
import time
import string
import glob
import datetime
import subprocess

def getCvsVersion(fileName, fullPath):
    # extract CVS version.
    baseDir = os.path.dirname(fullPath)
    cvsFileName = os.path.join(baseDir, 'CVS', 'Entries')    
    cvsVer=''
    if os.path.exists(cvsFileName):
        file = open(cvsFileName, 'r')
        cvsLines = file.readlines()
        for line in cvsLines:
            splitVals = line.split('/')        
            if len(splitVals)>2 and splitVals[1]==fileName:
                cvsVer = splitVals[2] 
    return cvsVer

def getSvnVersion(fileName, fullPath):
    # extract SVN version.
    baseDir = os.path.dirname(fullPath)
    svnFileName = os.path.join(baseDir, '.svn', 'entries')
    
    fileLines = []
    svnVer ={}
    inFile = 0
    counter = 11
    if os.path.exists(svnFileName):
        file = open(svnFileName, 'r')
        svnLines = file.readlines()
        for line in svnLines:
            if re.findall(re.compile(r'^' + fileName), line):
                inFile = 1
            if inFile:
                fileLines.append(line)
                counter = counter - 1
                if counter == 0:
                    break
    if inFile:
        svnVer['type'] = fileLines[1][0:-1]            
        svnVer['textLastUpdate'] = fileLines[6][0:-1]            
        svnVer['checkSum'] = fileLines[7][0:-1]            
        svnVer['lastChange'] = fileLines[8][0:-1]            
        svnVer['version'] = fileLines[9][0:-1]            
        svnVer['userName'] = fileLines[10][0:-1]
    else:
        svnVer = []
    return svnVer

def getGitVersion(fileName, fullPath, gitPath):
    # extract GIT version.
    baseDir = os.path.dirname(fullPath)
    gitFileName = os.path.join(baseDir, fileName)
    
    fileLines = []
    svnVer = {}
    inFile = 0
    counter = 11
    if os.path.exists(gitFileName):
        out_repo = subprocess.call(["git", "--git-dir", os.path.join(gitPath,'.git'), '--work-tree', baseDir, "ls-files", fileName, "--error-unmatch"])
        print out_repo
        if out_repo != 1:
            output = subprocess.check_output(["git", "--git-dir", os.path.join(gitPath,'.git'), '--work-tree', baseDir, "ls-files", fileName, "--error-unmatch"])
            print output
            gitVer = 0.1
        else:
            gitVer = []
    return gitVer

def readTxtFile(file, dirName="."):
    file = os.path.join(dirName, file)
    strRet = ''
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            if line[0]=='#':
                continue
            else:
                strRet += line
    return strRet

def extractFileDetails(file, seperator=",", dirName="."):

    details = []
    file = os.path.join(dirName, file);
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            if line[0]=='#':
                continue
            elif line[0]=='\n':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details


