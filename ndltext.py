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


def wrapText(text, padding, width = 70, indent = 0, comment = '%'):
    text = ' ' + text
    posList = [0]
    outText = ''
    endPoint = width
    while endPoint<len(text):
        pos = text[0:endPoint].rfind(' ')
        posList.append(pos)
        endPoint = pos + width
    padStr = padding
    for posNo in range(len(posList)-1):
        outText+= comment + padStr + text[posList[posNo]+1:posList[posNo+1]] + '\n'
        if indent>0:
            padStr = padding
            for num in range(indent):
                padStr += ' '    
    outText += comment + padStr + text[posList[-1]+1:-1] + '\n'
        
    return outText

