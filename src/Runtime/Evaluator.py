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
        
        # If-else:
        if node == 'if-else':
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