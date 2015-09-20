#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import shutil
import time
import datetime
sys.path.append('..')
import ndlcgi
import ndlcal

def printTodo(baseName, todoDetails):
    string = '<li><a href="../today/todo.cgi?file=' + baseName + '">' + todoDetails['title'] + '</a> by ' + todoDetails['endTime'].strftime('%A, %d %b') + ' [<a href="../today/editTodo.cgi?file=' + baseName + '">edit</a>]' + ' [<a href="../today/doneTodo.cgi?file=' + baseName + '">done</a>][<a href="../today/today.cgi?today=' + todoDetails['endTime'].strftime('%Y_%m_%d') + '">today</a>]</li>'
    return string


def printAppointment(baseName, appointDir, appDetails):
  string = ''
  if appDetails['type'] == ndlcal.appNum['Diary']:
    string += '<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'
  elif appDetails['type'] == ndlcal.appNum['Conference']:
    string += 'Conference:\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + ' (finishes ' + appDetails['endTime'].strftime('%A, %d') + ')</a>'
  elif appDetails['type'] == ndlcal.appNum['Deadline']:
    string += 'Deadline:\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'
  elif appDetails['type'] == ndlcal.appNum['Holiday']:
    string += 'Holiday:\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'
  elif appDetails['type'] == ndlcal.appNum['Visit']:
    string += 'Visit:\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + ' (finishes ' + appDetails['endTime'].strftime('%A, %d') + ')</a>'
  elif appDetails['type'] == ndlcal.appNum['Visitor']:
    string += 'Visitor:\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + ' (finishes ' + appDetails['endTime'].strftime('%A, %d') + ')</a>'
  elif int(appDetails['length']) < 24:
    if int(appDetails['length']) == 0:
      string += appDetails['startTime'].strftime('%H:%M') + '\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'

    else:
      string += appDetails['startTime'].strftime('%H:%M') + '-' + appDetails['endTime'].strftime('%H:%M') + '\t<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'
  elif int(appDetails['length']) == 24:
    string += '<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + '</a>'
  else:
    string += '<a href="../calendar/appointment.cgi?file=' + baseName + '&dir=' + appointDir + '">' + appDetails['title'] + ' (finishes ' + appDetails['endTime'].strftime('%A, %d') + ')</a>'
  string += '&nbsp;[<a href="../calendar/editAppointment.cgi?file=' + baseName + '&dir=' + appointDir + '&return=../today/today.cgi">edit</a>]'
  string += ' [<a href="../calendar/doneAppointment.cgi?file=' + baseName + '&dir=' + appointDir + '&return=../today/today.cgi">done</a>]'
  string += ' [<a href="../today/today.cgi?today=' + appDetails['startTime'].strftime('%Y_%m_%d') + '">today</a>]'
  string += '<br>'
  return string

def jsPrepareForm(formName, appDetails):
  out = '''<script><!--
  function loadCalEditor() 
  {
    dateFormPopulate(''' + formName + ''', ''' + formName + '''.startDay, ''' + str(appDetails['startTime'].day) + ''', ''' + formName + '''.startMonth, ''' + str(appDetails['startTime'].month) + ''', ''' + formName + '''.startYear, ''' + str(appDetails['startTime'].year) + ''');
    dateFormPopulate(''' + formName + ''', ''' + formName + '''.endDay, ''' + str(appDetails['endTime'].day) + ''', ''' + formName + '''.endMonth, ''' + str(appDetails['endTime'].month) + ''', ''' + formName + '''.endYear, ''' + str(appDetails['endTime'].year) + ''');
    selectFormSet(''' + formName + ''', ''' + formName + '''.type, ''' + str(appDetails['type']) + ''');
  }
  // -->
  </script>'''
  return out

def printFormHtml(formName, appDetails, dirToShow, requestedFile, submitScript):
  
  out = '''<form method="POST" action="./''' + submitScript + '''" onSubmit="return validateForm( this );" name="'''
  out += formName
  out += '''">

  <blockquote>
  <table>
  <tr>'''
  out += ndlcgi.formDateEntry(formName, 'startDay', appDetails['startTime'].day, 'startMonth', appDetails['startTime'].month, 'startYear', appDetails['startTime'].year)
  out += '''<td><b>Time</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'startHour', appDetails['startTime'].strftime('%H'), 10)
  out += ndlcgi.formInput(formName, 'text', 'startMin', appDetails['startTime'].strftime('%M'), 10)
  out += '''</td>
  </tr>'''
  out += ndlcgi.formDateEntry(formName, 'endDay', appDetails['endTime'].day, 'endMonth', appDetails['endTime'].month, 'endYear', appDetails['endTime'].year)
  out += '''<td><b>Time</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'endHour', appDetails['endTime'].strftime('%H'), 10)
  out += ndlcgi.formInput(formName, 'text', 'endMin', appDetails['endTime'].strftime('%M'), 10)
  out += '''</td>
  </tr>
  </table>
  <table>
  <tr>
  <td align = "left"><b>Title</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'title', appDetails['title'], 20)
  out += '''</td>
  <td align = "left"><b>Type</b>*</td>
  <td><select name="type" size="1"'''
  out += ' value=' + str(appDetails['type']) + '>'
  out += '''              '''
  keys = ndlcal.appNum.keys()
  keys.sort()
  for key in keys:
    out += '<option value=' + str(ndlcal.appNum[key]) + '>' + key + '</option>\n'

  out +='''</select>
  </td>
  </tr>
  <tr>
  <td align = "left"><b>Venue</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'venue', appDetails['venue'], 20)
  out += '''</td>'''
  out += '''<td align="left"><b>Length</b>*</td>
  <td>'''
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Speaker</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'speaker', appDetails['speaker'], 20)
  out += '''</td>
  </tr>
  <tr>
  <td align="left"><b>Length</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'length', appDetails['length'], 20)
  out += '''</td>
  </tr>
  </table>
  <table width=80%>
  <tr>
  <td align = "left"><b>Notes File</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'notesFile', appDetails['notesFile'], 20, 1)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.formTextArea(formName, 'notes', appDetails['notes'], 5, 40, 1)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes File</b>*</td>
  <td>'''
  out += ndlcgi.formInput(formName, 'text', 'notesHtmlFile', appDetails['notesHtmlFile'], 20)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Notes</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.formTextArea(formName, 'notesHtml', appDetails['notesHtml'], 5, 40)
  out += '''</td>
  </tr>
  <tr>
  <td align = "left"><b>Extra</b>*</td>
  <td colspan="6">'''
  out += ndlcgi.formTextArea(formName, 'extra', appDetails['extra'], 5, 40, 1)
  out += '''</td>
  </tr>'''
  #<tr>
  #<td align = "left"><b>E-mail</b>*</td>
  #<td colspan="3">
  #<input type=text name="email" onchange="checkEmail( this );" SIZE=25>
  #</td>
  #</tr>
  out += '''</table>
  * Indicates required field.
  </blockquote>
  <input type=submit value="Submit Form">
  <input type=reset value="Reset Form">'''
  if requestedFile:
    out += '''<input type="hidden" name="origFileName" value="''' + os.path.join(dirToShow, requestedFile) + '''">'''    
    out += '''<input type="hidden" name="origNotesFile" value="''' + os.path.join(dirToShow, 'notes', appDetails['notesFile']) + '''">'''    
    out += '''<input type="hidden" name="origNotesHtmlFile" value="''' + os.path.join(dirToShow, 'notesHtml', appDetails['notesHtmlFile']) + '''">'''    
  else:
    out += '''<input type="hidden" name="origFileName" value="">'''
    out += '''<input type="hidden" name="origNotesFile" value="">'''    
    out += '''<input type="hidden" name="origNotesHtmlFile" value="">'''    
  out += '''<input type="hidden" name="user" value="''' + os.environ['REMOTE_USER'] + '''">'''
  out += '''</form>'''
  return out

def readFormKeys(form):

  fieldDict = {}
  for key in form.keys():
    fieldDict[key] = form[key];

  startMin = int(fieldDict['startMin'].value)
  del fieldDict['startMin']
  startHour = int(fieldDict['startHour'].value)
  del fieldDict['startHour']
  startDay = int(fieldDict['startDay'].value)
  del fieldDict['startDay']
  startMonth = int(fieldDict['startMonth'].value)
  del fieldDict['startMonth']
  startYear = int(fieldDict['startYear'].value)
  del fieldDict['startYear']
  endMin = int(fieldDict['endMin'].value)
  del fieldDict['endMin']
  endHour = int(fieldDict['endHour'].value)
  del fieldDict['endHour']
  endDay = int(fieldDict['endDay'].value)
  del fieldDict['endDay']
  endMonth = int(fieldDict['endMonth'].value)
  del fieldDict['endMonth']
  endYear = int(fieldDict['endYear'].value)
  del fieldDict['endYear']
  if fieldDict['notesFile'].value == 'None':
    fieldDict['notesText'] = ''
  else:
    fieldDict['notesText'] = fieldDict['notes'].value
  if fieldDict.has_key('notes'):
    del fieldDict['notes']
  if fieldDict['notesHtmlFile'].value == 'None':
    fieldDict['notesHtmlText'] = ''
  else:
    fieldDict['notesHtmlText'] = fieldDict['notesHtml'].value
  if fieldDict.has_key('notesHtml'):
    del fieldDict['notesHtml']

  if not fieldDict.has_key('origFileName'):
    fieldDict['origFileName'] =  ''
  if not fieldDict.has_key('origNotesFile'):
    fieldDict['origNotesFile'] = ''
  appType = 'Appointment'
  if fieldDict.has_key('type'):
    appType = ndlcal.reverseApp(int(fieldDict['type'].value))
  fieldDict['type'].value = appType

  if not fieldDict.has_key('origNotesHtmlFile'):
    fieldDict['origNotesHtmlFile'] = ''

  fieldDict['startTime'] = datetime.datetime(startYear, startMonth, startDay, startHour, startMin)
  fieldDict['endTime'] = datetime.datetime(endYear, endMonth, endDay, endHour, endMin)
  lengthTuple = fieldDict['endTime'] - fieldDict['startTime']
  length = lengthTuple.days*24 + lengthTuple.seconds/(60*60)
  fieldDict['length'].value = length
  return fieldDict

def moveOrigFiles(fieldDict):
  # Check whether original file exists ... move if it does.
  if fieldDict['origFileName']:
    if os.path.exists(fieldDict['origFileName'].value):
      shutil.move(fieldDict['origFileName'].value, fieldDict['origFileName'].value + '~')
  if fieldDict['origNotesFile']:
    if os.path.exists(fieldDict['origNotesFile'].value):
      shutil.move(fieldDict['origNotesFile'].value, fieldDict['origNotesFile'].value + '~')
  if fieldDict['origNotesHtmlFile']:
    if os.path.exists(fieldDict['origNotesHtmlFile'].value):
      shutil.move(fieldDict['origNotesHtmlFile'].value, fieldDict['origNotesHtmlFile'].value + '~')

  del fieldDict['origFileName']
  del fieldDict['origNotesFile']
  del fieldDict['origNotesHtmlFile']
  return fieldDict

def writeNotes(fieldDict, notesPath):
  if not fieldDict['notesFile'].value == 'None':
    writePath = os.path.join(notesPath, 'notes')
    if not os.path.exists(writePath):
      os.mkdir(writePath)
    fieldDict['notesFile'].value = ndlcgi.novelFileName(fieldDict['notesFile'].value, writePath)
    fileName = os.path.join(writePath, fieldDict['notesHtmlFile'].value)
    f = open(fileName, 'w')
    f.write(fieldDict['notesText'])
    f.close()
  del fieldDict['notesText']

  if not fieldDict['notesHtmlFile'].value == 'None':
    writePath = os.path.join(notesPath, 'notesHtml')
    if not os.path.exists(writePath):
      os.mkdir(writePath)
    fieldDict['notesHtmlFile'].value = ndlcgi.novelFileName(fieldDict['notesHtmlFile'].value, writePath)
    fileName = os.path.join(writePath, fieldDict['notesHtmlFile'].value)
    f = open(fileName, 'w')
    f.write(fieldDict['notesHtmlText'])
    f.close()
  del fieldDict['notesHtmlText']
  return fieldDict

def writeAppointment(fieldDict, fileName):
  del fieldDict['startTime']
  del fieldDict['endTime']

  timeStamp = time.strftime('%A %d %b %Y at %H:%M')
  fileOut = '# Created at ' + timeStamp + '\n'

  keys = fieldDict.keys()
  keys.sort()
  for key in keys:
    fileOut += key + '|' + str(fieldDict[key].value) + '\n'

  # Write to file
  f = open(fileName, 'w')
  f.write(fileOut)
  f.close()

def returnToday():
  url = '''../today/today.cgi'''
  string = '''<div class="section"><META HTTP-EQUIV="Refresh" CONTENT="0; URL=''' + url + '''">'''
  #string = message
  string += '''<a href="''' + url + '''">Click here if not forwarded</a></div>'''
  #todayHeader.txt contains the pages' headers
  todayHeader = ndlcgi.readTxtFile('./today/todayHeader.txt')
  #todayFooter.txt contains the pages' footers
  todayFooter = ndlcgi.readTxtFile('./today/todayFooter.txt')
  #todayStyle.txt contains the pages' style
  todayStyle = ndlcgi.readTxtFile('./today/todayStyle.txt')
  timeStamp = time.strftime('%A %d %b %Y at %H:%M')

  ndlcgi.writeToScreen(string, todayStyle, 'Edit Succesful', todayHeader, todayFooter, timeStamp)
