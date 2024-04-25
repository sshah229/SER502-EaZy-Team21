import re

def tokenize(code):
    keywords = set(['keyword', 'spec_char', 'datatype', 'boolean'])
    tokens = re.findall(r'\b\w+\b|\'(?:[^\'\\]|\\.)*\'|"(?:[^"\\]|\\.)*"', code)
    tokens = [token.strip("'\"") for token in tokens]
    tokenized = []
    for token in tokens:
        try:
            if token in keywords:
                tokenized.append(('KEYWORD', token))
            elif token.startswith('num'):
                tokenized.append(('NUM', token.split('(')[1].strip(')')))
            elif token.startswith('str'):
                tokenized.append(('STRING', token.split('(')[1].strip(')')))
            elif token.startswith('id'):
                tokenized.append(('ID', token.split('(')[1].strip(')')))
            elif token.startswith('bool'):
                tokenized.append(('BOOL', token.split('(')[1].strip(')')))
            elif token.startswith('\'') or token.startswith('"'):
                tokenized.append(('STRING', token))
            elif token.startswith('('):
                tokenized.append(('LPAREN', token))
            elif token.startswith(')'):
                tokenized.append(('RPAREN', token))
            elif token.startswith('{'):
                tokenized.append(('LBRACE', token))
            elif token.startswith('}'):
                tokenized.append(('RBRACE', token))
            elif token == ';':
                tokenized.append(('SEMICOLON', token))
            elif token in ['+', '-', '*', '/', '%', '==', '<', '>', '<=', '>=', '=']:
                tokenized.append(('OPERATOR', token))
            elif token in ['and', 'or', 'not', 'if', 'else', 'for-loop', 'in', 'range', 'display', 'return', 'sup', 'peaceout']:
                tokenized.append(('KEYWORD', token))
            elif token.startswith('#'):
                tokenized.append(('COMMENT', token))
            else:
                tokenized.append(('UNKNOWN', token))
        except IndexError as e:
            print(f"Error: {e} - Token: {token}")
    return tokenized

# Sample code input
code = '''
keyword('sup').
keyword('peaceout').
keyword('int').
keyword('str').
keyword('bool').
keyword('True').
keyword('False').
keyword('for-loop').
keyword('in').
keyword('range').
keyword('if').
keyword('else').
keyword('display').
keyword('return').

spec_char('!').
spec_char('\\').
spec_char('#').
spec_char('$').
spec_char('&').
spec_char('(').
spec_char(')').
spec_char('*').
spec_char('+').
spec_char(',').
spec_char('-').
spec_char('.').
spec_char('/').
spec_char(':').
spec_char(';').
spec_char('<').
spec_char('=').
spec_char('>').
spec_char('?').
spec_char('@').
spec_char('~').
spec_char('%').
spec_char('^').

datatype('int').
datatype('str').
datatype('bool').

boolean('Sahi').
boolean('Galat').

%:-use_rendering(svgtree).
:-table expr/3, expr2/3, expr3/3, bool_expr/3, bool_expr2/3.

% numbers
num(num(pos,N1)) --> [N], {atom_number(N, N1)}.
num(num(neg,N1)) --> ['-'], [N], {atom_number(N, N1)}.
num(num(pos,N1)) --> ['+'], [N], {atom_number(N, N1)}.

...
'''

tokens = tokenize(code)
for token in tokens:
    print(token)
