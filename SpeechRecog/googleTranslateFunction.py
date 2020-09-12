#pip install googletrans

import googletrans
from googletrans import Translator

class Translate(object):
    def DAVIDtranslator(self, text):
        # Takes in a same string and returns the message
        # In the language of the users choice
        words = text.split(" ")
        start = words.index("translate")
        indexWords = ["in", "to", "into"]
        language = None
        for word in indexWords:
            if words[-2] == word:
                language = words[-1]
                if language == "Chinese":
                    language = "chinese (simplified)"
                words = " ".join(words[start+1:-2])
                break
        if language == None: 
            language = "english"
            words = " ".join(words[start+1:])
        translator = Translator()
        result = translator.translate(words, dest = language)
        answer = result.text
        return answer

def testDAVIDtranslator():
    print('Testing DAVIDtranslator()...', end='')
    sample1 = "D.A.V.I.D., translate I am asleep into Spanish"
    assert(DAVIDtranslator(sample1) == "Estoy dormido")
    sample2 = "D.A.V.I.D., translate I am asleep into Spanish"
    assert(DAVIDtranslator(sample2) == "Estoy dormido")
    sample3 = "D.A.V.I.D., translate That is good into German"
    assert(DAVIDtranslator(sample3) == "Das ist gut")
    sample4 = "D.A.V.I.D., translate Das ist gut"
    assert(DAVIDtranslator(sample4) == "It's good")
    sample5 = "D.A.V.I.D., translate I don't know into Chinese"
    assert(DAVIDtranslator(sample5) == "我不知道")
    sample6 = "D.A.V.I.D., translate 我不知道 into English"
    assert(DAVIDtranslator(sample6) == "I do not know")
    print('Passed')
#testDAVIDtranslator()