# creates file with inputed text
def textToFile(text):
    testFile = open(r"myFile.txt", "w+")
    testFile.write(text)
    testFile.close()

text = "Hello world. This is a test. I love CMU."
textToFile(text)

# converts text of multiple lines into a list of sentences
def convertTextToLines(file):
    fileString = findFile(file)
    currFile = open(fileString, "rt")
    readString = currFile.read()
    readList = []
    lastSplitIndex = 0
    currString = ""
    punctuation = [".", "!", "?"]
    for i in range(len(readString)):
        if (readString[i] in punctuation):
            if (i == len(readString) - 1):
                currString = readString[lastSplitIndex:i]
            else:
                currString = readString[lastSplitIndex:i] + " \n"
            withoutPunc = ""
            for char in currString:
                if (char not in punctuation):
                    withoutPunc += char
            if (withoutPunc[0] == " "):
                withoutPunc = withoutPunc[1:]
            readList.append(withoutPunc)
            lastSplitIndex = i
            withoutPunc = ""
    if (readList != []):
        return readList
    else: 
        return readString

# finds the correct text file name by adding .txt or not
def findFile(file):
    fileString = ""
    if (".txt" in file):
        fileString = f"{file}"
    else:
        fileString = f"{file}.txt"
    return fileString

# reads file and returns text
def fileToText(file):
    fileString  = findFile(file)
    newText = convertTextToLines(file)
    currFile = open(fileString, "w+")
    currFile.seek(0)
    currFile.writelines(newText)
    currFile.close()
    currFile = open(fileString, "r+")
    returnString = currFile.read()
    return returnString

fileName = "myFile.txt"
print(fileToText(fileName))

