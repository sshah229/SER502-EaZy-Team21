from ast import parse
import os,sys
from pyswip import Prolog

sys.path.insert(0,  os.getcwd() + '/src/compiler')

from tokenizer import EaZy_Tokenizer
from evaluator import Evaluator

def test_case(file_path):
    file = open(file_path, "r")
    program = file.read()
    
    #Tokenizer
    Token = Tokenizer()
    tokens = Token.tokenize_Program(program)
    
    #Parser
    plg = Prolog()
    plg.consult(os.getcwd() + '/src/compiler' + "/" + 'parser.pl')
    query = "program(T, " + str(tokens) + ", [])."
    
    parse_tree = ''
    
    for solution in plg.query(query):
        parse_tree = solution['T']
    print(parse_tree)
    ev = Evaluator()
    ev.evaluate(parse_tree)

#Update the name of the test files once they are made.
test_case(os.getcwd()+"/tests/test.txt")
test_case(os.getcwd()+"/tests/test.txt")