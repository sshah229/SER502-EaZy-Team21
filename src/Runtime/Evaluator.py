class Evaluator:

    def __init__(self):
        self.env = {}
        self.functions = {}
        self.default_val = {'int':0, 'str': '', 'bool':False}
        self.return_val = 0

    def setEnv(self, id, type, val):
        self.env[id] = {'type':type, 'val':val}

    def readTree(self, T):
        T = T.strip()
        leaves = []
        start = 0

        # Node
        i = start
        while i < len(T):
            if T[i] == '(':
                node = T[:i].strip()
                start = i + 1
                break
            i += 1
        # print('Node ',node)

        # Children
        i = start
        bracketCount = 0
        while i < len(T):
            if T[i] == '(':
                bracketCount += 1
            elif T[i] == ')':
                bracketCount -= 1
                if bracketCount == -1:
                    leaves.append(T[start:i].strip())
            elif T[i] == ',' and bracketCount == 0:
                leaves.append(T[start:i].strip())
                start = i+1
            i += 1
        
        return node, leaves
    
    def evaluate(self, T):
        node, leaves = self.readTree(T)

        # Numbers:
        if node == 'int':
            val = int(leaves[0])
            return val
        
        # Strings:
        if node == 'str':
            return leaves[0]
        
        # Boolean:
        if node == 'bool':
            return leaves[0] == 'Sahi'
        
        # Identifiers:
        elif node == 'id':
            # TODO: init error
            return self.env[leaves[0]]['val']
        
        # Arithmetic Expressions:
        elif node == 'add':
            return self.evaluate(leaves[0]) + self.evaluate(leaves[1])
        elif node == 'subtract':
            return self.evaluate(leaves[0]) - self.evaluate(leaves[1])
        elif node == 'multiply':
            return self.evaluate(leaves[0]) * self.evaluate(leaves[1])
        elif node == 'divide':
            return int(self.evaluate(leaves[0]) / self.evaluate(leaves[1]))
        elif node == 'modulo':
            return self.evaluate(leaves[0]) % self.evaluate(leaves[1])

        # Boolean Expressions:
        elif node == 'OR':
            return self.evaluate(leaves[0]) or self.evaluate(leaves[1])
        elif node == 'AND':
            return self.evaluate(leaves[0]) and self.evaluate(leaves[1])
        elif node == 'equals':
            return self.evaluate(leaves[0]) == self.evaluate(leaves[1])
        elif node == 'NOT':
            return not self.evaluate(leaves[0])
        
        # STATEMENTS
        elif node == 'stmt_list':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        
        # declaration
        elif node == 'dec':
            # TODO: multiple initialization errors
            self.setEnv(leaves[1], leaves[0], self.defaultValues[leaves[0]])
        elif node == 'decAssign':
            # TODO: multiple initialization errors
            self.setEnv(leaves[1], leaves[0], self.evaluate(leaves[2]))

        elif node == 'display':
            print(self.evaluate(leaves[0]))

        elif node == 'assign':
            self.env[leaves[0]]['val'] = self.evaluate(leaves[1])
        elif node == 'addAssign':
            self.env[leaves[0]]['val'] += self.evaluate(leaves[1])
        elif node == 'subAssign':
            self.env[leaves[0]]['val'] -= self.evaluate(leaves[1])
        elif node == 'mulAssign':
            self.env[leaves[0]]['val'] *= self.evaluate(leaves[1])
        elif node == 'divAssign':
            self.env[leaves[0]]['val'] /= self.evaluate(leaves[1])

        # If-else:
        elif node == 'if-else':
            if self.evaluate(leaves[0]):
                self.evaluate(leaves[1])
            else:
                self.evaluate(leaves[2])
        
        # For-loop:
        elif node == "for_T":
            self.evaluate(leaves[0])
            while(self.evaluate(leaves[1])):
                self.evaluate(leaves[2])
                self.evaluate(leaves[3])
        elif node == 'for_Range':
            iterator = self.env[leaves[0]]
            iterator['val'] = self.evaluate(leaves[1])
            stopVal = self.evaluate(leaves[2])
            while iterator['val'] <= stopVal:
                self.evaluate(leaves[3])
                iterator['val'] += 1
        
        elif node == 'display':
            print(self.evaluate(leaves[0]))

        # Function call:
        elif node == 'no_func':
            pass
        elif node == 'List_of_func':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        elif node == 'function':
            self.defineFunc(leaves)
        elif node == 'call':
            #print('call', leaves)
            functionEvaluator = Evaluator()
            function = self.functions[leaves[0]]
            args = []
            functionEvaluator.functions = self.functions

            if len(function['parameters']):
                self.parseArguments(leaves[1], args)
                for i in range(len(args)):
                    functionEvaluator.setEnv(function['parameters'][i][1], function['parameters'][i][0], args[i])
            functionEvaluator.evaluate(function['tree'])
            return functionEvaluator.returnValue
        elif node == 'return':
            self.returnValue = self.evaluate(leaves[0])
            
        # Program:
        elif node == "Program":
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])

        return 0
    
    def parseParameters(self, Tree, Accumulator):
        node, leaves = self.readTree(Tree)
        if node == 'nonePmt':
            return
        elif node == 'pmt':
            Accumulator.append(leaves)  # ['int', 'a']
        elif node == 'pmtList':
            self.parseParameters(leaves[0], Accumulator)
            self.parseParameters(leaves[1], Accumulator)

    def parseArguments(self, Tree, Accumulator):
        node, leaves = self.readTree(Tree)
        if node == 'noneArg':
            return
        elif node == 'argList':
            self.parseArguments(leaves[0], Accumulator)
            self.parseArguments(leaves[1], Accumulator)
        else:
            Accumulator.append(self.evaluate(Tree))
    
if __name__ == '__main__':
    eval = Evaluator()
    eval.env['x'] = {'type': 'int', 'val': 5}
    s = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), add(2, 5)), display(id(y))))'
    s1 = 'forT( assign(id(x), 0), compareLesser(id(x), 10), assign(id(x), add(id(x), 1)), stmt_list( display(id(x)), display(id(y)) ) )'
    s2 = 'id(x)'
    s3 = 'num(6)'
    s4 = 'display(id(y))'
    
    acc = []
    eval.parseArguments('argList(id(x), num(pos, 6))', acc)
    print(acc)