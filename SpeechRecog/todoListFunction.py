
"""
Inputs:
    Add "Blank" to my to do list
    Remove "Blank" from my to do list
        If not there, say "This is not on your to do list"
    Read me my to do list


Output:
    I have added "Blank" to your to do list
    ...


"""
# Basic understanding taken from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO

def readTodoList(path):
    with open(path, "rt") as f:
        return f.read()

def getTodoListData(path):
    toDoList = readTodoList(path)
    entries = toDoList.splitlines()
    return entries

def textToTask(text):
    textList = text.split(" ")
    vals = []
    keys = ["add","remove","delete"]
    for i in keys:
        if i in textList:
            vals.append(textList.index(i))
    cut = textList[min(vals)+1:-5]
    task = " ".join(cut)
    return task, textList[min(vals)]

#Hardcodes name as todolist
def textToFile(path, text):
    testFile = open(r"todoList.txt", "w+")
    testFile.write(text)
    testFile.close()

def createList(entries):
    data = "\n".join(entries)
    return data

def addTask(path, task):
    entries = getTodoListData(path)
    entries.append(task)
    textToFile(path, createList(entries))
    return f"{task} was added to your to do list"

def removeTask(path, task):
    entries = getTodoListData(path)
    if task in entries:
        entries.remove(task)
        textToFile(path, createList(entries))
        return f"{task} was removed from your to do list."
    else:
        return "I'm sorry, but it appears that is not in your to do list."

def readTask(path):
    entries = getTodoListData(path)
    if len(entries) == 0:
        return "There is nothing on your to do list"
    else:
        message = "Today on your to do list: "
        entries = ". ".join(entries)
        return message + entries

def DAVIDtoDoList(text):
    path = "todoList.txt"
    if ("read" in text):
        return readTask(path)
    else:
        task, key = textToTask(text)
        if key == "add":
            return addTask(path,task)
        elif (key == "remove") or (key == "delete"):
            return removeTask(path,task)