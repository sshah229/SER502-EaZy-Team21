class Evaluator:
    def __init__(self):
        self.env = {}
        self.functions = {}
        self.default_values = {'int': 0, 'str': '', 'bool': False}
        self.return_value = 0

    def set_env(self, id_, type_, val):
        self.env[id_] = {'type': type_, 'val': val}

    def read_tree(self, tree):
        tree = tree.strip()
        leaves = []
        start = 0
        i = start
        while i < len(tree):
            if tree[i] == '(':
                node = tree[:i].strip()
                start = i + 1
                break
            i += 1
        i = start
        brackets_count = 0
        while i < len(tree):
            if tree[i] == '(':
                brackets_count += 1
            elif tree[i] == ')':
                brackets_count -= 1
                if brackets_count == -1:
                    leaves.append(tree[start:i].strip())
            elif tree[i] == ',' and brackets_count == 0:
                leaves.append(tree[start:i].strip())
                start = i + 1
            i += 1
        return node, leaves

    def evaluate(self, tree):
        node, leaves = self.read_tree(tree)
        if node == 'num':
            val = int(leaves[1])
            if leaves[0] == 'neg':
                val *= -1
            return val
        elif node == 'str':
            return leaves[0]
        elif node == 'bool':
            return leaves[0] == 'True'
        elif node == 'id':
            return self.env[leaves[0]]['val']
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
        elif node == 'stmt_list':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        elif node == 'dec':
            self.set_env(leaves[1], leaves[0], self.default_values[leaves[0]])
        elif node == 'decAssign':
            self.set_env(leaves[1], leaves[0], self.evaluate(leaves[2]))
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
        elif node == 'display':
            print(self.evaluate(leaves[0]))
        elif node == 'ifelse':
            if self.evaluate(leaves[0]):
                self.evaluate(leaves[1])
            else:
                self.evaluate(leaves[2])
        elif node == 'forT':
            self.evaluate(leaves[0])
            while(self.evaluate(leaves[1])):
                self.evaluate(leaves[2])
                self.evaluate(leaves[3])
        elif node == 'forR':
            iterator = self.env[leaves[0]]
            iterator['val'] = self.evaluate(leaves[1])
            stopVal = self.evaluate(leaves[2])
            while iterator['val'] <= stopVal:
                self.evaluate(leaves[3])
                iterator['val'] += 1
        elif node == 'noneFunc':
            pass
        elif node == 'funcList':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        elif node == 'func':
            self.define_func(leaves)
        elif node == 'call':
            function_evaluator = Evaluator()
            func = self.functions[leaves[0]]
            args = []
            function_evaluator.functions = self.functions
            if len(func['parameters']):
                self.parse_arguments(leaves[1], args)
                for i in range(len(args)):
                    function_evaluator.set_env(func['parameters'][i][1], func['parameters'][i][0], args[i])
            function_evaluator.evaluate(func['tree'])
            return function_evaluator.return_value
        elif node == 'return':
            self.return_value = self.evaluate(leaves[0])
        elif node == 'prog':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        return 0

    def parse_parameters(self, tree, accumulator):
        node, leaves = self.read_tree(tree)
        if node == 'nonePmt':
            return
        elif node == 'pmt':
            accumulator.append(leaves)
        elif node == 'pmtList':
            self.parse_parameters(leaves[0], accumulator)
            self.parse_parameters(leaves[1], accumulator)

    def parse_arguments(self, tree, accumulator):
        node, leaves = self.read_tree(tree)
        if node == 'noneArg':
            return
        elif node == 'argList':
            self.parse_arguments(leaves[0], accumulator)
            self.parse_arguments(leaves[1], accumulator)
        else:
            accumulator.append(self.evaluate(tree))

    def define_func(self, leaves):
        func_name = leaves[0]
        pmt_list = []
        self.parse_parameters(leaves[1], pmt_list)
        func_tree = leaves[2]
        self.functions[func_name] = {'parameters': pmt_list, 'tree': func_tree}


if __name__ == '__main__':
    evaluator = Evaluator()
    evaluator.env['x'] = {'type': 'int', 'val': 5}
    stmt = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))'
    acc = []
    evaluator.parse_arguments('argList(id(x), num(pos, 6))', acc)
    print(acc)
