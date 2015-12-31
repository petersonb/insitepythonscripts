# Validate Flatfile
# A work in progress
#
# Author : Brett Peterson - bpeterson@insitesoft.com

delimiter = '|'

def getFlatFile():
    filename = input("Enter file name (in same directory) or leave blank to use in.dat: ")
    if filename == "":
        filename = "in.dat"
    try:
        return open(filename)
    except:
        print("File not found. Does '{0}' exist in this directory?".format(filename))
        input("Press enter to let me die...")
        raise

def extractLines(infile):
    lineList = []
    for line in infile:
        lineList.append(line.strip())
    return lineList

def fileReport(lineList):
    # Count
    lineCount = len(lineList)
    print("There were {0} lines pulled from the file.".format(lineCount))
    # Average line character count
    total = 0
    for line in lineList:
        total += len(line)
    avg = total/lineCount
    print("There is an average line lenghth (characters) of {0}.".format(avg))

def reportProblem(lineNumber, line, problemMessage):
    print("\nLine: {0}\n{1}\n{2}\n".format(lineNumber, line, problemMessage))

def processFile(infile):
    lineList = extractLines(infile)
    if len(lineList) < 1:
        print("No lines in file")
        return
    infile.close()
    fileReport(lineList)
    return lineList

def validateLines(lineList):
    headerLine = lineList[0].split('|')
    expectedColumnCount = len(headerLine)
    print("\nExpecting {0} items per line as from header line\n{1}\n".format(expectedColumnCount, headerLine))
    lineNumber = 0
    validationProblemCount = 0
    for line in lineList:
        lineNumber += 1
        valid = validateLine(line, expectedColumnCount, lineNumber)
        if not valid:
            validationProblemCount += 1
    print("The validation finished with {0} issues".format(validationProblemCount))

def validateLine(line, expectedItems, lineNumber):
    line = line.replace(' ','')
    splitLine = line.split(delimiter)
    # Count
    if len(splitLine) != expectedItems:
        reportProblem(lineNumber, line, "Incorrect number of items")
        return False
    # Each item has double quotes around it
    for item in splitLine:
        if item.count('"') != 2:
        #if item[0] != '"' and item[-1] != '"':
            reportProblem(lineNumber, line, "Item does not contain pair of qotes on {0}.".format(item))
            return False
    return True
    

if __name__ == "__main__":
    infile = getFlatFile()
    lineList = processFile(infile)
    validateLines(lineList)
    input("Enter to kill me...")
