from pyswip import Prolog

from CodeTokenizer import CodeTokenizer
from Evaluator import Evaluator

if __name__=='__main__':
     # Open a program to Read
     file = open("function2.ez", "r")
     program =  file.read()
     
     # Tokenize the program according to grammar
     Tk = CodeTokenizer()
     tokens = Tk.tokenizeProgram(program)

     # Consult the parser to then generate a prolog query
     prolog = Prolog()
     prolog.consult('parser.pl') 
     query = "program(T, " + str(tokens) + ", [])."
     print(query)
     # Generating a parse tree for the query
     for soln in prolog.query(query):
          parseTree = soln['T']
          break
     
     # Evaluate and print out final environment
     eval = Evaluator()
     eval.evaluate(parseTree)
     print('Execution SUCCESS :)')
     print('Environment: ', eval.env)
     print('Parse Tree: ', parseTree)