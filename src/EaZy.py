import os, sys
from pyswip import Prolog

sys.path.insert(0, os.getcwd() + '/src/compiler')

from tokenizer import Tokenizer         # These files are assumed to be made at this point
# from evaluator import Evaluator

if __name__=='__main__':
     file = open("sample.ez", "r")
     program =  file.read()
     
     Tk = Tokenizer()
     tokens = Tk.tokenizeProgram(program)
     print(tokens)

     prolog = Prolog()
     prolog.consult('parser.pl') 
     query = "program(T, " + str(tokens) + ", [])."
     print(query)

     parseTree = ''
     for soln in prolog.query(query):
          parseTree = soln['T']
          break
     print(parseTree)