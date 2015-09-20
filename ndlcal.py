#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import time
import datetime
sys.path.append('..')
import ndlcgi


baseAppointmentDir = os.path.join("/home/neil/mlprojects", "appointments")
baseTodoDir = os.path.join("/home/neil/mlprojects", "todo")
baseSeminarDir = os.path.join("/home/neil/mlprojects", "seminars")
appNum = {'Appointment':1,
          'Conference':2,
          'Deadline':3,
          'Dentist':4,
          'Diary':5,
          'Holiday':6,
          'Flight':7,
          'Talk':8,
          'Todo':9,
          'Visit':10,
          'Visitor':11}


def printAdditionalKeys(appDetails):
  del appDetails['notesFile']
  del appDetails['notesHtmlFile']
  del appDetails['startTime']
  del appDetails['endTime']
  del appDetails['length']
  del appDetails['title']
  del appDetails['venue']
  del appDetails['type']
  del appDetails['speaker']
  del appDetails['user']
  del appDetails['done']
  string = ''
  keys = appDetails.keys()
  keys.sort()
  for key in keys:
    if appDetails[key]:
      string += '<br>' + key + ': ' + str(appDetails[key])
  string += appDetails['extra']
  return string

def appointmentDetails(requestedFile, dirToShow):
  fileToShow = os.path.join(dirToShow, requestedFile)
  details = ndlcgi.extractFileDetails(fileToShow, '|')
  appDetails = {}
  appDetails['affiliation'] = ''
  appDetails['webpage'] = ''
  appDetails['user'] = ''
  appDetails['extra'] = ''
  appDetails['title'] = ''
  appDetails['venue'] = ''
  appDetails['speaker'] = ''
  appDetails['type'] = 'Appointment'
  appDetails['length'] = ''
  appDetails['slides'] = ''
  appDetails['notes'] = ''
  appDetails['notesFile'] = 'None'
  appDetails['notesHtml'] = ''
  appDetails['notesHtmlFile'] = 'None'
  appDetails['done'] = 0
  for detail in details:
    if detail[0] == "notesFile" or detail[0] == "notes":
      appDetails['notesFile'] = detail[1]
      appDetails['notes'] += ndlcgi.readTxtLinesFile(os.path.join(dirToShow, 'notes', appDetails['notesFile']))
    elif detail[0] == "notesHtmlFile":
      appDetails['notesHtmlFile'] = detail[1]
      appDetails['notesHtml'] += ndlcgi.readTxtLinesFile(os.path.join(dirToShow, 'notesHtml', appDetails['notesHtmlFile']))
    elif detail[0] == "type":
      appDetails['type'] = appNum[detail[1]]
    else:
      appDetails[detail[0]] = detail[1]

  appointmentLength = datetime.timedelta(float(appDetails['length'])/24)
  baseFile = os.path.splitext(requestedFile)
  fileParts = baseFile[0].split('_')
  dateTimeString = fileParts[0] + '_' + fileParts[1] + '_' + fileParts[2] + '_' + fileParts[3]
  startTimeTuple = time.strptime(dateTimeString, '%Y_%m_%d_%H%M')
  appDetails['startTime'] = datetime.datetime(startTimeTuple[0], startTimeTuple[1], startTimeTuple[2], startTimeTuple[3], startTimeTuple[4])
  appDetails['endTime'] = appDetails['startTime'] + appointmentLength
  appDetails['ordinalEnd'] = appDetails['endTime'].toordinal()
  return appDetails

def reverseApp(number):
  for key in appNum.keys():
    if int(number) == appNum[key]:
      appType = key
      break
  return appType

