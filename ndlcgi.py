#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import glob
import time
import stat

def pamiLinks():
    return '''<ul>
    <li><a href="https://mc.manuscriptcentral.com/tpami-cs">PAMI Manuscript Central</a></li>
    <li><a href="http://jmlr.csail.mit.edu/manudb/center/manulist?action">JMLR Editing</a></li>
    <li></li>
    </ul>'''
def searchBox():
    return '''<table><tr><td><form method="get" action="http://www.google.com/search">

<input type="text"   name="q" size="31"
 maxlength="255" value="" />
<input type="submit" value="Google Search" /></td>
<tr>
<td>
<input type="radio"  name="sitesearch" value="" />
 The Web
<input type="radio"  name="sitesearch"
 value="cs.man.ac.uk" checked /> Manchester Computer Science<br />
</td>
</tr>
</table>
</form>'''

def usefulLocalLinks():
    return '''<ul>
    <li><a href="http://intranet.cs.man.ac.uk/ACSO/rooms/">Room Bookings</a></li>
    <li><a href="http://www.cs.man.ac.uk/~jls/rota.html">MLO Lunch Meetings</a></li>
    <li><a href="../seminars/seminars.cgi">Machine Learning Seminars</a></li>
    <li><a href="http://intranet.cs.man.ac.uk/Events_subweb/admin/">Workshop Registration List</a></li>
    </ul>'''

def googleScholarBox():
    return '''<!-- Google Scholar -->
    <form method="get" action="http://scholar.google.com/scholar">
      <table bgcolor="#FFFFFF">
        <tr>
          <td>
          <a href="http://scholar.google.com/"> <img src="http://scholar.google.com/scholar/scholar_sm.gif" alt="Google Scholar" width="105" height="40" border="0" align="absmiddle" /></a>
          <input type="hidden" name="hl" value="en">
          <input type="text" name="q" size="25" maxlength="255" value="" />
          <input type="submit" name="btnG" value="Search" />
          </td>
        </tr>
      </table>
    </form>
    <!-- Google Scholar --> '''

def jsImportScript():
    return '<script src="../../lib/formLib.js"></script>'

def jsValidateForm(formName, requiredTexts, requiredSelects):
    out = '''<script><!--
    function validateForm ( form ) {
    requiredText = new Array('''
    while(len(requiredTexts)>1):
        out += '"' + requiredTexts.pop() + '"' + ', '
    if(len(requiredTexts)):
        out += '"' + requiredTexts.pop() + '"'
    out += ''');
    requiredSelect = new Array('''
    while(len(requiredSelects)>1):
        out += '"' + requiredSelects.pop() + '"' + ', '
    if(len(requiredTexts)):
        out += '"' + requiredSelects.pop() + '"'
    out += ''');
          return requireValues ('''
    out += formName
    out += ''', requiredText   ) &&
    requireSelects ( '''
    out += formName +''', requiredSelect  ) &&
                 checkProblems (  );
    }
    // -->
    </script>'''
    return out


def formDateEntry(formName, dayField, dayVal, monthField, monthVal, yearField, yearVal):
    out = '''<td><b>Day</b></td>
    <td><select name="''' + dayField + '''" value=''' + str(dayVal) + '''></select></td>
    <td><b>Month</b></td>
    <td><select name="''' + monthField + '''" value=''' + str(monthVal) + '''
    onChange="dateFormChangeMonth(''' + formName + ''', ''' + dayField + ''', ''' + monthField + ''', ''' + yearField + ''')">
    <Option value=1>January</Option>
    <Option value=2>February</Option>
    <Option value=3>March</Option>
    <Option value=4>April</Option>
    <Option value=5>May</Option>
    <Option value=6>June</Option>
    <Option value=7>July</Option>
    <Option value=8>August</Option>
    <Option value=9>September</Option>
    <Option value=10>October</Option>
    <Option value=11>November</Option>
    <Option value=12>December</Option>
    </select></td>
    <td><b>Year</b></td>
    <td><select name="''' + yearField + '''" ''' + '''value=''' + str(yearVal) + '''></select></td>'''
    return out



def formInput(formName, type, name, value, size, hidden=0):
    if hidden:
        return '<input type="hidden" name="' + name + '" value="' + value + '">'
    else:
        return '<input type="' + type + '" name="' + name + '" value="' + value + '"size="' + str(size) + '">'


def formTextArea(formName, name, value, rows, cols, hidden=0):
    if hidden:
        return '<input type="hidden" name="' + name + '" value="' + value + '">'
    else:
        return '<textarea name="' + name + '" rows="' + str(rows) + ' cols="' + str(cols) + '">' + value + '</textarea>'


def monthName(number):
    months={
        '01':'January',
        '02':'February',
        '03':'March',
        '04':'April',
        '05':'May',
        '06':'June',
        '07':'July',
        '08':'August',
        '09':'September',
        '10':'October',
        '11':'November',
        '12':'December'
        }
    return months[number]

def readTxtFile(file):
    strRet = ''
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            strRet += line
    return strRet

def readTxtLinesFile(file):
    strRet = ''
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            strRet += line
    return strRet

def readTxtLinesFileBreak(file):
    strRet = ''
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            strRet += line + '<br>'
    return strRet

def extractFileDetails(file, seperator=","):

    details = []
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            if line[0]=='#':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details


def writeToScreen(string, style = '', title='', header='', footer='', time=''):
    if len(string)>0:
	if len(title)>0:
       	    string = "<head><title>" + title + "</title></head>\n" + string
	if len(header)>0:
            string = header + string
	if len(style)>0:
            string = style + string
	if len(time)>0:
            string += "<p align=\"center\">Page generated on " + time + ", maintained by Neil D. Lawrence" + "</p>"
	if len(footer)>0:
            string += footer
        print "Content-type: text/html\n"
        sys.stdout.write(string)


def getReference(keyName):
    h = httplib.HTTP('www.cs.man.ac.uk')
    print "Getting publication " + keyName + ".\n"
    h.putrequest('GET', '/neill-bin/publications/bibpage.cgi?keyName=' + keyName + '&header=0&printAbstract=1')
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        print "... succesful."
    else:
        print "Error " + errcode + ", " + errmsg
    f = h.getfile()
    lines = f.read()
    f.close()
    return lines
    
def readTxtFile(file):
    strRet = ''
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            strRet += line
    return strRet
    
def extractFileDetails(file, seperator=","):
    details = []
    if os.path.exists(file):
        fileHandle = open(file, 'r');
        fileLines = fileHandle.readlines()
        fileHandle.close()
        for line in fileLines:
            if line[0]=='#':
                continue
            else:
                details.append(string.splitfields(line, seperator))
    else:
        sys.exit(0)

    for i in range(len(details)):
        for j in range(len(details[i])):
            details[i][j] = details[i][j].strip()

    return details


def writeToFile(file, string, style = '', title='', header='', footer='', time=''):
    if len(string)>0:
	if len(title)>0:
       	    string = "<head><title>" + title + "</title></head>\n" + string
	if len(header)>0:
            string = header + string
	if len(style)>0:
            string = style + string
	if len(time)>0:
            string += "<p align=\"center\">Page last updated on " + time + " by Neil D. Lawrence" + "</p>"
	if len(footer)>0:
            string += footer
        fileHandle = open(file, 'w')
        fileHandle.write(string)
        fileHandle.close()


def novelFileName(baseName, directory):

    fileName = os.path.join(directory, baseName)
    counter = 0
    while os.path.exists(fileName):
        counter = counter + 1
        parts = os.path.splitext(baseName)
        baseName = parts[0] + '_' + str(counter) + parts[1]
        fileName = os.path.join(directory, baseName)
    return baseName

