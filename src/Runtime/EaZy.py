import os, sys
from pyswip import Prolog

sys.path.insert(0, os.getcwd() + '/src/compiler')

from tokenizer import Tokenizer         # These files are assumed to be made at this point
from evaluator import Evaluator

if __name__=='__main__':
     file = open("data/sample.ez", "r")
     program =  file.read()
     
     Tk = Tokenizer()
     tokens = Tk.tokenizeProgram(program)
     
     prolog = Prolog()
     prolog.consult('src/compiler/parser.pl') 
     query = "program(T, " + str(tokens) + ", [])."