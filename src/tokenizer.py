class Tokenizer:

    def __init__(self) -> None:

        self.keywords = set(['sup', 'peaceout', 'int', 'str', 'bool', 'Sahi', 'Galat', 'for-loop', 'in', 'range', 'if', 'else', 'display', 'return'])

        self.comp = set(['+=', '-=', '*=', '/=', '>=', '==', '<='])
        self.op = set(['+', '-', '*', '/', '%', '<', '>', '='])
        self.dl = set([';', '(', ')', '{', '}', ',', '?', ':'])

    def tokenize(self,text):
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
            return ['for-loop'] + self.tokenize(text[len('for-loop'):])
        
        # string
        if text[0]=='"':
            i=1
            while(i<len(text)):
                if text[i] == '"':
                    tokens.append(text[0]) # "
                    tokens.append(text[1:i]) # string
                    tokens.append(text[i]) # "
                    return tokens + self.tokenize(text[i+1:])  
                i+=1

        # Comments
        if text.startswith('@'):
            i=2
            while i<len(text):
                if text[i]=='$' and text[i-1]=='$':
                    return self.tokenize(text[i+1:])
                i+=1

        # Syntactic sugar 
        if text[:2] in self.comp:
            tokens.append(text[:2])
            return tokens + self.tokenize(text[2:])  


        # Operators
        if text[0] in self.op or text[0] in self.dl:
            tokens.append(text[:1])
            return tokens + self.tokenize(text[1:])  

        # everything else
        i=0
        while(i<len(text)):
            if text[i] in self.dl or text[i] in self.op:
                tokens.append(text[:i])
                return tokens + self.tokenize(text[i:])
            elif text[i] == ' ':
                tokens.append(text[:i])
                return tokens + self.tokenize(text[i+1:])
            i+=1
        
        return [text]

    def tokenizeProgram(self, program):
        tokens = []
        for line in program.split('\n'):
            tokens += self.tokenize(line)
        return tokens

if __name__ == "__main__":
    Tk = Tokenizer()

    tokens = []
    def testcases():
        helloworld = 'hello world'
        print(Tk.tokenizeProgram(helloworld)==['hello', 'world'])
        
        forloop = 'for-loop(k in range(1, 5)) {i += 3;}'
        print(Tk.tokenizeProgram(forloop)==['for-loop', '(', 'k', 'in', 'range', 
                                            '(', '1', ',', '5', ')', ')', '{', 'i', 
                                            '+=', '3', ';', '}'])
        
        ternary = 'x == 12? display eZ : s = 12'
        print(Tk.tokenize(ternary)==['x', '==', '12', '?', 'display', 
                                       'eZ', ':', 's', '=', '12'])
        
        comment = '@ This is a Comment @'
        print(Tk.tokenize(comment)==['@', 'This', 'is', 'a', 'Comment', '@'])

        if_else = 'if (x + 1 == 3) { display "this is EZ"; }'
        print(Tk.tokenize(if_else)==['if', '(', 'x', '+', '1', '==', '3', ')', '{', 'display', 
                                   '"', 'this is EZ', '"', ';', '}'])
        
        prog = 'sup int x; peacout'
        print(Tk.tokenize(prog)==['sup', 'int', 'x', ';', 'peacout'])

        bool_ = 'bool s = Galat ;'
        print(Tk.tokenize(bool_) == ['bool', 's', '=', 'Galat', ';'])


    testcases()