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
     # print(query)
     #parseTree = ''
     for soln in prolog.query(query):
          parseTree = soln['T']
          break
     # print(parseTree)
     #exit()

     # EVALUATE
     eval = Evaluator()
     eval.evaluate(parseTree)
     print('PROGRAM EXECUTED')
     print('ENV: ', eval.env)
     print('FN: ', eval.functions)