import unittest
from unittest import result
import os, sys

sys.path.insert(0, os.getcwd() + '/src/')
from tokenizer import Tokenizer


class Testing(unittest.TestCase):
    testCase_1 = "str SS;\nbool SER502 = Galat;\nint Group = 6 + 3 * 5;\nx = \"SSSA\";"
    expected_1 = ['str', 'SS', ';', 'bool', 'SER502', '=', 'Galat', ';', 'int', 'Group', '=', '6', '+', '3', '*', '5', ';', 'x', '=', '"', 'SSSA', '"', ';']

    testCase_2 = "y = not y;\nbool X = Sahi or Galat;"
    expected_2 = ['y', '=', 'not', 'y', ';', 'bool', 'X', '=', 'Sahi', 'or', 'Galat', ';']

    testCase_3 = "int A = x+y+z/4;"
    expected_3 = ['int', 'a', '=', 'x', '+', 'y' , '+', 'z', '/', '4', ';']

    testCase_4 = "sup\n int N;\n str SASS;"
    expected_4 = ['sup', 'int', 'N', ';','str', 'SASS', ';']
    
    testCase_5 = "bool X = Sahi or Galat;"
    expected_5 = ['bool', 'X', '=', 'Sahi', 'or', 'Galat', ';']
    
    testCase_6 = "x == 5 ? display Sahi : display Galat;"
    expected_6 = ['x', '==', '5', '?', 'display', 'Sahi', ':', 'display', 'Galat', ';']
    
    testCase_7 = "if (x == 5) { display Sahi; } else { display Galat; }"
    expected_7 = ['if', '(', 'x', '==', '5', ')', '{', 'display', 'Sahi', ';', '}', 'else', '{', 'display', 'Galat', ';', '}']
    
    testCase_8 = "for-loop (int i = 0; i < 5; i += 1) { display i; }"
    expected_8 = ['for-loop', '(', 'int', 'i', '=', '0', ';', 'i', '<', '5', ';', 'i', '+=', '1', ')', '{', 'display', 'i', ';', '}']
    
    testCase_9 = "func int add(int a, int b) { return a + b; }"
    expected_9 = ['func', 'int', 'add', '(', 'int', 'a', ',', 'int', 'b', ')', '{', 'return', 'a', '+', 'b', ';', '}']

    def test1(self):
        result = Tokenizer(Testing.testCase_1)
        self.assertEqual(result, Testing.expected_1)
    
    def test2(self):
        result = Tokenizer(Testing.testCase_2)
        self.assertEqual(result, Testing.expected_2)

    def test3(self):
        result = Tokenizer(Testing.testCase_3)
        self.assertEqual(result, Testing.expected_3)
    
    def test4(self):
        result = Tokenizer(Testing.testCase_4)
        self.assertEqual(result, Testing.expected_4)
    
    def test4(self):
        result = Tokenizer(Testing.testCase_4)
        self.assertEqual(result, Testing.expected_4)
    
    def test5(self):
        result = Tokenizer(Testing.testCase_5)
        self.assertEqual(result, Testing.expected_5)
    
    def test6(self):
        result = Tokenizer(Testing.testCase_6)
        self.assertEqual(result, Testing.expected_6)
    
    def test7(self):
        result = Tokenizer(Testing.testCase_7)
        self.assertEqual(result, Testing.expected_7)
    
    def test8(self):
        result = Tokenizer(Testing.testCase_8)
        self.assertEqual(result, Testing.expected_8)
    
    def test9(self):
        result = Tokenizer(Testing.testCase_9)
        self.assertEqual(result, Testing.expected_9)

if __name__ == '__main__':
    unittest.main()