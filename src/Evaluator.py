class Evaluator:

    # Initializing the evaluator
    def __init__(self):
        self.env = {}
        self.functions = {}
        self.defaultValues = {'int': 0, 'str': '', 'bool': False}
        self.returnValue = 0

    # Setting up constructors for the data types
    def setEnv(self, id, type, val):
        self.env[id] = {'Type': type, 'Val': val}

    def readTree(self, T):
        T = T.strip()
        leaves = []
        start = 0
        # Reading tree nodes
        i = start
        while i < len(T):
            if T[i] == '(':
                node = T[:i].strip()
                start = i+1
                break
            i += 1
        
        # Reading children nodes
        i = start
        paranthesisCount = 0
        while i < len(T):
            if T[i] == '(':
                paranthesisCount += 1
            elif T[i] == ')':
                paranthesisCount -= 1
                if paranthesisCount == -1:
                    leaves.append(T[start:i].strip())
            elif T[i] == ',' and paranthesisCount == 0:
                leaves.append(T[start:i].strip())
                start = i+1
            i += 1
        return node, leaves

    # Evaluating the parse Tree
    def evaluate(self, tree):
        node, leaves = self.readTree(tree)
        
        # Evaluating numbers
        if node == 'num':
            val = int(leaves[1])    # Second node contains the value
            if leaves[0] == 'neg':  # If negative number
                val *= -1
            return val

        # 
        elif node == 'str':
            return leaves[0]
        elif node == 'bool':
            return leaves[0] == 'Sahi'
        elif node == 'id':
            return self.env[leaves[0]]['val']

        # Evaluating Arithmetic expressions
        elif node == 't_add':
            return self.evaluate(leaves[0]) + self.evaluate(leaves[1])
        elif node == 't_sub':
            return self.evaluate(leaves[0]) - self.evaluate(leaves[1])
        elif node == 't_mul':
            return self.evaluate(leaves[0]) * self.evaluate(leaves[1])
        elif node == 't_div':
            return int(self.evaluate(leaves[0]) / self.evaluate(leaves[1]))
        elif node == 't_mod':
            return self.evaluate(leaves[0]) % self.evaluate(leaves[1])

        # Evaluating Booleans
        elif node == 'or':
            return self.evaluate(leaves[0]) or self.evaluate(leaves[1])
        elif node == 'and':
            return self.evaluate(leaves[0]) or self.evaluate(leaves[1])
        elif node == 'equals':
            return self.evaluate(leaves[0]) == self.evaluate(leaves[1])
        elif node == 'lt':
            return self.evaluate(leaves[0]) < self.evaluate(leaves[1])
        elif node == 'gt':
            return self.evaluate(leaves[0]) > self.evaluate(leaves[1])
        elif node == 'lteq':
            return self.evaluate(leaves[0]) <= self.evaluate(leaves[1])
        elif node == 'gteq':
            return self.evaluate(leaves[0]) >= self.evaluate(leaves[1])
        elif node == 'not':
            return not self.evaluate(leaves[0])

        # STATEMENTS
        elif node == 'stmt_list':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        # declaration
        elif node == 'dec':
            # TODO: multiple init errors
            self.setEnv(leaves[1], leaves[0], self.defaultValues[leaves[0]])
        elif node == 'decAssign':
            # TODO: multiple init errors
            self.setEnv(leaves[1], leaves[0], self.evaluate(leaves[2]))

        # Evaluating syntactic sugar assignments
        elif node == 'assign':
            self.env[leaves[0]]['val'] = self.evaluate(leaves[1])
        elif node == 'addAssign':
            self.env[leaves[0]]['val'] += self.evaluate(leaves[1])
        elif node == 'subAssign':
            self.env[leaves[0]]['val'] -= self.evaluate(leaves[1])
        elif node == 'mulAssign':
            self.env[leaves[0]]['val'] *= self.evaluate(leaves[1])
        elif node == 'divAssign':
            self.env[leaves[0]]['val'] = int(self.evaluate(
                self.env[leaves[0]]['val'] / leaves[1]))
        
        # Displaying strings
        elif node == 'display':
            print(self.evaluate(leaves[0]))
        
        # Evaluating Conditionals
        elif node == 'ifelse':
            if self.evaluate(leaves[0]):
                self.evaluate(leaves[1])
            else:
                self.evaluate(leaves[2])

        # for-loop
        elif node == 'forT':    # Traditional for loop
            self.evaluate(leaves[0])
            while(self.evaluate(leaves[1])):
                self.evaluate(leaves[2])
                self.evaluate(leaves[3])
        elif node == 'forR':    # Ranged for loop
            iterator = self.env[leaves[0]]
            iterator['val'] = self.evaluate(leaves[1])
            stopVal = self.evaluate(leaves[2])
            while iterator['val'] <= stopVal:
                self.evaluate(leaves[3])
                iterator['val'] += 1

        # Evaluating functions
        elif node == 'noneFunc':    # No functions are defined in program
            pass
        elif node == 'funcList':    # If there are functions instantiated
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        elif node == 'func':
            self.defineFunc(leaves)
        elif node == 'call':        # When functions are called from the main body
            functionEvaluator = Evaluator()
            func = self.functions[leaves[0]]
            args = []
            functionEvaluator.functions = self.functions

            if len(func['parameters']):
                self.parseArguments(leaves[1], args)
                for i in range(len(args)):
                    functionEvaluator.setEnv(func['parameters'][i][1], func['parameters'][i][0], args[i])
            functionEvaluator.evaluate(func['tree'])
            return functionEvaluator.returnValue
        elif node == 'return':
            self.returnValue = self.evaluate(leaves[0])

        # Evaluate the program
        elif node == 'prog':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])

        return 0

    def parseParameters(self, tree, Accumulator):
        node, leaves = self.readTree(tree)
        if node == 'nonePmt':
            return
        elif node == 'pmt':
            Accumulator.append(leaves)  # ['int', 'a']
        elif node == 'pmtList':
            self.parseParameters(leaves[0], Accumulator)
            self.parseParameters(leaves[1], Accumulator)

    def parseArguments(self, tree, Accumulator):
        node, leaves = self.readTree(tree)
        if node == 'noneArg':
            return
        elif node == 'argList':
            self.parseArguments(leaves[0], Accumulator)
            self.parseArguments(leaves[1], Accumulator)
        else:
            Accumulator.append(self.evaluate(tree))

    def defineFunc(self, leaves):
        funcName = leaves[0]
        pmtList = []
        self.parseParameters(leaves[1], pmtList)    # Get parameters from the parse tree
        funcTree = leaves[2]
        self.functions[funcName] = {'parameters': pmtList, 'tree': funcTree}


if __name__ == '__main__':
    eval = Evaluator()
