import re
'''
Dict of word/abbreviation mapped to synonyms/expansions

Example Input:
    Input 1 :     NH #: 44
    Output 1:     
        National HighWay Number: 44
    
    Input 2:    ph #: +91-9848012345
    Output 2:
        telephone Number: +91-9848012345
        mobile Number: +91-9848012345
        landline Number: +91-9848012345

Note: based on dict, transulation can enter infinite loop ex: # mapping to ##
'''

class WordTransulator:
    def __init__(self, transulator):
        self.transulator = transulator

    def __init__(self):
        self.transulator = {
            "#": ("Number",),
            "No": ("Number",),
            "tele": ("telephone",),
            "ph": ("telephone",),
            "Rd": ("Road",),
            "telephone": ("mobile", "landline"),
            "Road": ("Boulevard", "Way"),
            "NH": ("National HighWay",),
            "mobile": ("telephone",)
        }

    def transulate_word(self, word):
        result = []
        words_to_transulate = [word]
        while words_to_transulate:
            tr_words = self.transulator.get(words_to_transulate[-1]) 
            if not tr_words:
                for index, ch in enumerate(word):
                    tr_chs = self.transulator.get(ch) or (ch,)
                    if tr_chs != (ch,):
                        tr_words = [word[0:index]+tr_ch+word[index+1:] for tr_ch in tr_chs]
                        break;

            del words_to_transulate[-1] # remove the processed input

            if tr_words:
                for w in tr_words:
                    if w not in result:
                        result.append(w)
                        words_to_transulate.append(w)
            if word in result:
                result.remove(word)
        return result

    def transulate(self, text):
        transulation_texts = [text]
        transulated_str = []
        while transulation_texts:
            input_text, tr_words_list = transulation_texts[-1], [[]]
            del transulation_texts[-1]
            for word in re.split(r' ', input_text):
                if word:
                    tr_words = self.transulate_word(word.strip()) or [word.strip()]
                    temp = []
                    for new_word in tr_words:
                        temp += [ prev_words + [new_word] for prev_words in tr_words_list ] # list of list of words
                    tr_words_list = temp # list of list of words i.e. list of statements
                    
            
            for tr_words in tr_words_list:
                tr_text = " ".join(tr_words) #form the statement from words
                if (tr_text not in transulated_str):
                    transulated_str.append(tr_text)
                    transulation_texts.append(tr_text)
                    
        if text in transulated_str:
            transulated_str.remove(text) # remove the input text in case of no transulation

        return list(transulated_str)

if __name__ == '__main__':
    text = input("Please Enter the text for transulation : ")
    print("Transulated text are \n")
    for text in WordTransulator().transulate(text):
        print (text)