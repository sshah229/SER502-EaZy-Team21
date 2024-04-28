class CodeTokenizer:

    def __init__(self) -> None:

        # Reserved Keywords
        self.keywords = set(['sup', 'peaceout', 'int', 'str', 'bool', 'Sahi', 'Galat', 'for-loop', 'in', 'range', 'if', 'else', 'display', 'return'])

        # Compound Operators
        self.compound_operators = set(['+=', '-=', '*=', '/=', '>=', '==', '<='])

        # Operators
        self.operators = set(['+', '-', '*', '/', '%', '<', '>', '='])

        # Delimiters
        self.delimiters = set([';', '(', ')', '{', '}', ',', '?', ':'])

    def tokenize(self, text):
        text = text.strip()
        tokens = []

        if not len(text):
            return []

        # Check for Keywords
        if text in self.keywords:
            return [text]

        # Check for 'for-loop'
        if text.startswith('for-loop'):
            return ['for-loop'] + self.tokenize(text[len('for-loop'):])

        # Check for String
        if text[0] == '"':
            i = 1
            while i < len(text):
                if text[i] == '"':
                    tokens.append(text[0])  # "
                    tokens.append(text[1:i])  # string
                    tokens.append(text[i])  # "
                    return tokens + self.tokenize(text[i + 1:])
                i += 1

        # Check for Comments
        if text.startswith('@@'):
            i = 2
            while i < len(text):
                if text[i] == '@' and text[i - 1] == '@':
                    return self.tokenize(text[i + 1:])
                i += 1

        # Check for Compound Operators
        if text[:2] in self.compound_operators:
            tokens.append(text[:2])
            return tokens + self.tokenize(text[2:])

        # Check for Operators and Delimiters
        if text[0] in self.operators or text[0] in self.delimiters:
            tokens.append(text[:1])
            return tokens + self.tokenize(text[1:])

        # Tokenize Everything Else
        i = 0
        while i < len(text):
            if text[i] in self.delimiters or text[i] in self.operators:
                tokens.append(text[:i])
                return tokens + self.tokenize(text[i:])
            elif text[i] == ' ':
                tokens.append(text[:i])
                return tokens + self.tokenize(text[i + 1:])
            i += 1

        return [text]

    def tokenizeProgram(self, program):
        tokens = []
        for line in program.split('\n'):
            tokens += self.tokenize(line)
        return tokens

if __name__ == "__main__":
    tokenizer = CodeTokenizer()

    # Test Cases
    def testcases():
        # Test Case 1
        helloworld = 'hello world'
        print(tokenizer.tokenizeProgram(helloworld) == ['hello', 'world'])

        # Test Case 2
        forloop = 'for-loop(k in range(1, 5)) {i += 3;}'
        print(tokenizer.tokenizeProgram(forloop) == ['for-loop', '(', 'k', 'in', 'range',
                                                     '(', '1', ',', '5', ')', ')', '{', 'i',
                                                     '+=', '3', ';', '}'])

        # Test Case 3
        ternary = 'x == 12? display eZ : s = 12'
        print(tokenizer.tokenize(ternary) == ['x', '==', '12', '?', 'display',
                                              'eZ', ':', 's', '=', '12'])

        # Test Case 4
        comment = '@@ This is a Comment @@'
        print(tokenizer.tokenize(comment) == [])

        # Test Case 5
        if_else = 'if (x + 1 == 3) { display "this is EZ"; }'
        print(tokenizer.tokenize(if_else) == ['if', '(', 'x', '+', '1', '==', '3', ')', '{', 'display',
                                              '"', 'this is EZ', '"', ';', '}'])

        # Test Case 6
        prog = 'sup int x; peacout'
        print(tokenizer.tokenize(prog) == ['sup', 'int', 'x', ';', 'peacout'])

        # Test Case 7
        syntactic_sugar = 'a += 2 ;'
        print(tokenizer.tokenize(syntactic_sugar) == ['a', '+=', '2', ';'])


    testcases()
