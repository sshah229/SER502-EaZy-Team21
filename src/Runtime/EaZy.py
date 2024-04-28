from pyswip import Prolog

from Tokenizer import Tokenizer         # These files are assumed to be made at this point
from Evaluator import Evaluator

if __name__=='__main__':
     file = open("sample.ez", "r")
     program =  file.read()
     
     Tk = Tokenizer()
     tokens = Tk.tokenizeProgram(program)
     
     prolog = Prolog()
     prolog.consult('parser.pl') 
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