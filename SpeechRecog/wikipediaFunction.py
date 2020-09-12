import wikipedia as wiki

# Moldule from https://pypi.org/project/wikipedia/

def getDAVIDFacts(text):
    # Returns the first two lines of wikipedia regarding the specific question
    textList = text.split(" ")
    index = textList.index("about")
    textList = textList[index+1:]
    text = " ".join(textList)
    senLength = 2
    try:
        result = (wiki.summary(text, sentences = senLength))
    except:
        try:
            result = (wiki.summary(text[4:], sentences = senLength))
        except:
            result = "I didn't understand your quesiton. Can you ask again?"
    return result