#!/usr/bin/env python

import re
import os

tex_directories = os.environ['BIBINPUTS'].split(':') + os.environ['TEXINPUTS'].split(':')
def replaceNotation(texfile_lines, oldNotation, newNotation):
    """Replace one notation in a tex file with another."""
    #    openBracketList ='\(|\[|\{'
    #closeBracketList = '\)|\]|\}'
    #mathSymbol = '=|+|-\)|\]|\}'
    #subSuperList = '\^|_'
    #notationReg = '[' + openBracketList +'|'+ closeBracketList +'|' + subSuperList+'|'+ '\s' + oldNotation \^|_|\s|\]|\}|oldNotation
    filename = ''
    for line in texfile_lines:
        filename = filename + line

    terminate = '[^\w|_]'
    startMath = re.escape('$')
    notReg = re.compile(r'([' + startMath + ']' + '[^' + startMath + ']*' + terminate + ')' + oldNotation + '(' + terminate + ')')
    matches = notReg.findall(filename)
    return matches

def extractBibFiles(texfile_lines):
    bib_files = []
    matchBib = re.compile(r"""\\bibliography{([^}]*)}""")
    matchBib2 = re.compile(r"""\\begin{btSect}.*{([^}]*)}""")

    full_text = ''
    for line in texfile_lines:
        full_text += line

    lineBib = matchBib.findall(full_text)
    if lineBib:
        for bib in lineBib:
            bib_files = bib_files + bib.split(',')
    lineBib2 = matchBib2.findall(full_text)
    if lineBib2:
        for bib in lineBib2:
            bib_files = bib_files + bib.split(',')

    return bib_files

def expand_dir(filename, directories=None):
    """Find the location of a file within the tex directories."""
    file_dir = os.path.dirname(filename)

    # build list of directories to search for file.
    if directories == None:
        directories = [file_dir]
        filename = os.path.basename(filename)
    elif len(file_dir)>0:
        if file_dir not in directories:
            directories.append(file_dir)

    for directory in tex_directories:
        if directory not in directories:
            directories.append(directory)

    # Open the tex file
    texFileHandle = None
    for directory in directories:
        full_filename = os.path.join(directory, filename)
        if os.path.exists(full_filename):
            return full_filename
    return None

def readlines(filename, directories=None):
    """Read the lines of the given tex file, searching in relevant direcctories."""
    full_filename = expand_dir(filename, directories)
    if full_filename is None:
        return None
    texFileHandle = open(full_filename, 'r')
    
    # Read the texfile
    return texFileHandle.readlines()

def substituteInputs(filename, directories=None):
    """Substitute input commands in the tex with the original file."""
    # Check if its a macro
    if filename[0] == '#': # it's a macro
        return None

    print('Substituting in:', filename)
    texfile_lines = readlines()
    if texfile_lines is None:
        return None

    newLines = []
    # Avoid parsing defined commands in notation def.
    for line in texfile_lines:
        if type(line) is not str:
            print('ERROR')
            print(line)
        if not line[0] == '%':
            matchInp = re.compile(r"""\\newsection *{([^}]*)} *{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(2)), directories)
                if subs:
                    replaceString = '\\section{' + match.group(1) + '}' + '\n'*2 + '\n'.join(subs)
                    line = line.replace(match.group(0), replaceString)

            matchInp = re.compile(r"""\\newsubsection *{([^}]*)} *{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(2)), directories)
                if subs:
                    replaceString = '\\subsection{' + match.group(1) + '}' + '\n'*2 + '\n'.join(subs)
                    line = line.replace(match.group(0), replaceString)

            matchInp = re.compile(r"""\\newsubsubsection *{([^}]*)} *{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(2)), directories)
                if subs:
                    replaceString = '\\subsubsection{' + match.group(1) + '}' + '\n'*2 + '\n'.join(subs)
                    line = line.replace(match.group(0), replaceString)
                    
            matchInp = re.compile(r"""\\inputdiagram{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(1)), directories)
                if subs:
                    replaceString = '\\small\n' + '\n'.join(subs) + '\\vspace{0.5cm}\n'
                    line = line.replace(match.group(0), replaceString)

            matches = [r"""\\input{([^}]*)}""",
                       r"""\\includetalkfile{([^}]*)}""",
                       r"""\\includecvfile{([^}]*)}"""]
            for match_string in matches:
                matchInp = re.compile(match_string)
                for match in matchInp.finditer(line):
                    subs = substituteInputs(inputFileName(match.group(1)), directories)
                    if subs:
                        line = line.replace(match.group(0), '\n'.join(subs))

        
        for l in line.split('\n'):
            newLines.append(l)

    
    return newLines

def inputFileName(filename):
    if filename[-4:] == '.tex':
        return filename
    else:
        return filename + '.tex'

def processTexFile(filename):
    texFileHandle = open(filename, 'r')
    texfile_lines = texFileHandle.readlines()
    inpList = extractInputs(texfile_lines)
    for inp in inpList:
        if not inp[0] == '#':
            if inp[-4:] == '.tex':
                texfile_lines += processTexFile(inp)
            else:
                texfile_lines += processTexFile(inp + '.tex')
    return texfile_lines

def extractInputs(texfile_lines):
    """Extract input files from a tex file."""
    inp_list = []

    matches = [r"""\\newsection *{[^}]*} *{([^}]*)}""",
               r"""\\newsubsection *{[^}]*} *{([^}]*)}""",
               r"""\\newsubsubsection *{[^}]*} *{([^}]*)}""",
               r"""\\includetalkfile{([^}]*)}""",
               r"""\\includecvfile{([^}]*)}""",
               r"""\\input *{([^}]*)}""",
               r"""\\input{([^}]*)}"""]
    full_text = ''
    for line in texfile_lines:
        if len(line)>0 and line[0] != '%':            
            for match_string in matches:
                matchInp = re.compile(match_string)
                lineInp = matchInp.findall(line)
                if lineInp:
                    for inp in lineInp:
                        if not inp[0] == '#':
                            inp_list += inp.split(',')


    return inp_list

def extractDiagrams(texfile_lines):
    """Extract diagrams from lines of a tex file"""
    diagramList = []
    matches = [r"""\\includegraphics *\[[^\]]*\] *{([^}]*)}""",
               r"""\\includegraphics<[^>]*>{([^}]*)}""",
               r"""\\includegraphics<[^>]*>\[[^\]]*\]{([^}]*)}""",
               r"""\\includegraphics{([^}]*)}"""]

    full_text = ''
    for line in texfile_lines:
        if len(line)>0 and line[0] != '%':
            full_text += line
    for match_string in matches:
        matchDiagram = re.compile(match_string)
        lineDiagram = matchDiagram.findall(full_text)
        if lineDiagram:
            for diagram in lineDiagram:
                if diagram[0] != '#':
                    diagramList += diagram.split(',')

    return diagramList

def extractCitations(texfile_lines):
     citations_list = []
     matchCite = re.compile(r"""\\cite[^\{]*{([^}\\#]+)}""")
     fullText = ''
     for line in texfile_lines: 
         fullText += line
     lineCite = matchCite.findall(fullText)
     if lineCite:
         for cite in lineCite:
             if cite[0] != '#':
                 citations_list += cite.split(',')
     for i in range(len(citations_list)):
         for j in range(i+1, len(citations_list)):
             if citations_list[i] == citations_list[j]:
                  citations_list[j] = [];

     return citations_list

def makeBibFile(citations_list, bib_files):
    """Make a bib file from a list of citations."""
    if citations_list:
        citations_list.sort()
        crossRefList = []
        stringList = []
        out = ''
        # Get the location of the bibfiles
        bibDir = os.environ['BIBINPUTS'].split(':')

        # Regular expressions 
        matchBibField = re.compile(r"""(\@\w+{)""")
        matchCrossRef = re.compile(r"""\bcrossref\s*=\s*[\"|{](.*)[}|\"]""", re.IGNORECASE)
        matchString = re.compile(r"""\b\w*\s*=\s*(\w*),""")

        for dir in bibDir:
            if not dir:
                dir = '.'
            for filename in bib_files:
                if os.access(os.path.join(dir, filename)+".bib", os.F_OK):
                    bibFileHandle = open(os.path.join(dir, filename) + ".bib", 'r')
                    bibFile = bibFileHandle.read()
                    # Split the bib file at the entries.
                    bibComp = matchBibField.split(bibFile)
                    for i in range(len(citations_list)):
                        if citations_list[i]:
                            if i>0 and citations_list[i] == citations_list[i-1]:
                                citations_list[i] = []
                                continue
                            for j in range(2, len(bibComp)):
                                entry = bibComp[j].split(',')
                                entry = entry[0].split('=')
                                if not entry[0].find(citations_list[i])==-1:
                                    #print entry[0]
                                    # Adds the entry to output
                                    out = out + bibComp[j-1] + bibComp[j]
                                    # Removes the citation from the list
                                    citations_list[i] = []
                                    crossRefs = matchCrossRef.findall(bibComp[j])
                                    if crossRefs:
                                        crossRefList = crossRefList + crossRefs
                                    else:                                        
                                        strings = matchString.findall(bibComp[j])
                                        if strings:
                                            for string in strings:
                                                if not stringList.count(string):
                                                    stringList.append(string)
                                    break
        return getBibStrings(stringList, bib_files) + out + getBibCrossRefs(crossRefList, bib_files)
    else:
        return ''
    
def getBibStrings(stringList, bib_files):
   if stringList:
       return makeBibFile(stringList, bib_files)
   else:
       return ''
      
def getBibCrossRefs(stringList, bib_files):
   if stringList:
       return makeBibFile(stringList, bib_files)
   else:
       return ''


def createBibFileGivenTex(texfile_lines):

   bib_files = extractBibFiles(texfile_lines)
   citations_list = extractCitations(texfile_lines)

   return makeBibFile(citations_list, bib_files)
