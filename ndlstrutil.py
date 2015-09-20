def tokenise(line, separator):
    bufferLine = ''
    field = ''
    inQuotes = 0
    splits = []
    for i in range(len(line)):
        # Check for toggling of quotes
        if line[i] == '"' and not bufferLine == '\\':
            inQuotes = not inQuotes
            bufferLine = line[i]
        else:
            # check for separator and end of field
            if not inQuotes and line[i]==separator:
                splits.append(field)
                bufferLine = separator
                field = ''
                continue
            if line[i] == '\n':
                splits.append(field)
                field = ''
            # remove whitespace at end and start of field
            if not inQuotes and line[i]==' ':
                bufferLine = ' '
                continue
            # check for escape character
            if line[i]=='\\':
                # check if it is escaped!
                if bufferLine=='\\':
                    field = field + line[i]
                    bufferLine == ''
                    continue
                else:
                    bufferLine == '\\'                    
            else:
                field = field + line[i]
    return splits

def validateEmail(address):
    if len(address)>7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", address) != None:
            return 1
    return 0

def stringFromFile(fileName):
    fileHandle = open(fileName, 'r')
    readLines = fileHandle.readlines()
    fileHandle.close()
    text = ''
    for line in readLines:
        text += line
        text += '\n'
    return text
