class Tokenizer:

    def __init__(self) -> None:

        self.keywords = set(['sup', 'peaceout', 'int', 'str', 'bool', 'True', 'False', 'for-loop', 'in', 'range', 'if', 'else', 'display', 'return'])

        self.comp = set(['+=', '-=', '*=', '/=', '>=', '==', '<='])
        self.op = set(['+', '-', '*', '/', '%', '<', '>', '='])
        self.dl = set([';', '(', ')', '{', '}', ',', '?', ':'])

    def tokenizer1(self,text):
        #print('TEXT:', text)
        text=text.strip()
        tokens = []

        if not len(text):
            return []
        
        # KEYWORD
        if text in self.keywords:
            return [text]

        # for-loop
        if text.startswith('for-loop'):
            return ['for-loop'] + self.tokenizer1(text[len('for-loop'):])
        
        # string
        if text[0]=='"':
            i=1
            while(i<len(text)):
                if text[i] == '"':
                    tokens.append(text[0]) # "
                    tokens.append(text[1:i]) # string
                    tokens.append(text[i]) # "
                    return tokens + self.tokenizer1(text[i+1:])  
                i+=1

    def tokenizeProgram(self, program):
        tokens = []
        for line in program.split('\n'):
            tokens += self.tokenizer1(line)
        return tokens

if __name__ == "__main__":
    Tk = Tokenizer()