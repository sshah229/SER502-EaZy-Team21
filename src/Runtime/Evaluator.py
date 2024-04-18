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
        # TODO write evaluator for different functionalities of the grammar