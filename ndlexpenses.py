#!/usr/bin/env python

import cgi, string, os
import cgitb; cgitb.enable()
import sys
import os
import shutil
import time
import datetime

import ndlcgi
import ndlcal

baseExpensesDir = os.path.join("/home/neil/mlprojects", "expenses")

def accountEntry():
    out = '''<td>&nbsp;Account Number:'''
    out += '''<select name="accountNumber", value=1>'''
    out += '''<Option value=1>AA000</option>'''
    out += '''<Option value=2>R01</option>'''
    out += '''<Option value=3>R201</option>'''
    out += '''<Option value=4>External</option>'''
    out += '''</select></td>'''
    return out

def categoryEntry():
    out = '''<td>&nbsp;Expense Category:'''
    out += '''<select name="accountNumber", value=1>'''
    out += '''<Option value=1>Travel</option>'''
    out += '''<Option value=2>Accommodation</option>'''
    out += '''<Option value=3>Subsistence</option>'''
    out += '''</select></td>'''
    return out

def reasonEntry():
    out ='''<td>Reason Incurred <input type="text", name="reasonIncurred", value="", size=15></td>'''
    return out

def expenseBox(formName, appDetails, submitScript):
    out = '<!-- Expense Box -->\n'
    out += '''<table><tr><td><form method="POST" action="./''' + submitScript + '''" onSubmit="return validateForm( this );" name="'''
    out += formName
    out += '''">'''
    out += ndlcgi.formDateEntry(formName, 'expenseTime', appDetails['endTime'].day, 'endMonth', appDetails['endTime'].month, 'endYear', appDetails['endTime'].year)

    out += reasonEntry()
    out += categoryEntry()
    out += accountEntry()
    out +='''</form></td></tr></table>'''
    return out
