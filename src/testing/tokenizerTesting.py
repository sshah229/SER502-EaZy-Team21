import unittest
from unittest import result
import os, sys

sys.path.insert(0, os.getcwd() + '/src/')
from tokenizer import tokenise


class Testing(unittest.TestCase):
    testCase_1 = "str SS;\nbool SER502 = Galat;\nint Group = 6 + 3 * 5;\nx = \"SSSA\";"
    expected_1 = ['str', 'SS', ';', 'bool', 'SER502', '=', 'Galat', ';', 'int', 'Group', '=', '6', '+', '3', '*', '5', ';', 'x', '=', '"', 'SSSA', '"', ';']

    testCase_2 = "y = not y;\nbool X = Sahi or Galat;"
    expected_2 = ['y', '=', 'not', 'y', ';', 'bool', 'X', '=', 'Sahi', 'or', 'Galat', ';']

    testCase_3 = "int A = x+y+z/4;"
    expected_3 = ['int', 'a', '=', 'x', '+', 'y' , '+', 'z', '/', '4', ';']

    testCase_4 = "sup\n int N;\n str SASS;"
    expected_4 = ['sup', 'int', 'N', ';','str', 'SASS', ';']

    def test1(self):
        result = tokenise(Testing.testCase_1)
        self.assertEqual(result, Testing.expected_1)
    
    def test2(self):
        result = tokenise(Testing.testCase_2)
        self.assertEqual(result, Testing.expected_2)

    def test3(self):
        result = tokenise(Testing.testCase_3)
        self.assertEqual(result, Testing.expected_3)
    
    def test4(self):
        result = tokenise(Testing.testCase_4)
        self. assertEqual(result, Testing.expected_4)

if __name__ == '__main__':
    unittest.main()