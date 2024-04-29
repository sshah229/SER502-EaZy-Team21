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





boolean('True').
boolean('False').



%:-use_rendering(svgtree).
:-table expr/3, expr2/3, expr3/3, bool_expr/3, bool_expr2/3.

% numbers
num(num(pos,N1)) --> [N], {atom_number(N, N1)}.
num(num(neg,N1)) --> ['-'], [N], {atom_number(N, N1)}.
num(num(pos,N1)) --> ['+'], [N], {atom_number(N, N1)}.



% strings
string(str(T)) --> ['\"'], [T], ['\"'], {atom_chars(T, TList), char(TList, [])}.
char --> [].
char --> [A], char, {is_alpha(A)}.
char --> [A], char, {atom_number(A, _)}.
char --> [A], char, {spec_char(A)}.
char --> [' '], char.

% identifiers
id(id(T)) --> [T], {not(keyword(T)) ,atom_chars(T, TList), isIdentifier(TList, [])}.
isIdentifier --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [].
id_suffix --> [A], id_suffix, {is_alpha(A)}.
id_suffix --> [N], id_suffix, {atom_number(N, _)}.

% arithmetic expressions
expr(t_add(T1,T2)) --> expr(T1), ['+'], expr2(T2).
expr(t_sub(T1,T2)) --> expr(T1), ['-'], expr2(T2).
expr(T) --> expr2(T).

expr2(t_mul(T1,T2)) --> expr2(T1), ['*'], expr3(T2).
expr2(t_div(T1,T2)) --> expr2(T1), ['/'], expr3(T2).
expr2(t_mod(T1,T2)) --> expr2(T1), ['%'], expr3(T2).
expr2(t_pow(T1,T2)) --> expr2(T1), ['^'], expr3(T2).
expr2(T) --> expr3(T).

expr3(T) --> num(T).
expr3(T) --> id(T).
expr3(T) --> ['('], expr(T) , [')'].

% boolean expressions

bool_expr(or(T1,T2)) --> bool_expr(T1), ['or'], bool_expr2(T2).
bool_expr(T) --> bool_expr2(T).

bool_expr2(and(T1,T2)) --> bool_expr2(T1), ['and'], bool_expr3(T2).
bool_expr2(T) --> bool_expr3(T).

% equality (boolean)
bool_expr3(equals(T1,T2)) -->  bool_expr(T1), ['=='], bool_expr(T2).
bool_expr3(equals(T1,T2)) -->  expr(T1), ['=='], expr(T2).
bool_expr3(equals(T1,T2)) -->  id(T1), ['=='], value(T2).

% arithmetic comparison (boolean)
bool_expr3(lt(T1,T2)) --> expr(T1), ['<'], expr(T2).
bool_expr3(gt(T1,T2)) --> expr(T1), ['>'], expr(T2). 
bool_expr3(lteq(T1,T2)) --> expr(T1), ['<='], expr(T2). 
bool_expr3(gteq(T1,T2)) --> expr(T1), ['>='], expr(T2).

bool_expr3(T) -->['('], bool_expr(T), [')'].
bool_expr3(not(T)) --> ['not'], bool_expr(T).
bool_expr3(T) --> bool(T).
bool_expr3(T) --> id(T).
bool(bool(T)) --> [T], {boolean(T)}.

% statements
stmt_list(T) --> stmt(T).
stmt_list(T) --> stmt(T), [';'].
stmt_list(T) --> stmt_block(T).
stmt_list(stmt_list(T1,T2)) --> stmt(T1), [';'], stmt_list(T2).
stmt_list(stmt_list(T1,T2)) --> stmt_block(T1), stmt_list(T2).



% declarations
value(T) --> bool_expr(T).
value(T) --> expr(T).
value(T) --> string(T).
value(call(T1,T2)) --> id_name(T1), ['('] , arg_list(T2), [')'].
id_name(T) --> [T], {not(keyword(T)) ,atom_chars(T, TList), isIdentifier(TList, [])}.
stmt(dec(T1,T2)) --> [T1], id_name(T2), {datatype(T1)}.
stmt(decAssign(T1,T2,T3)) --> [T1], id_name(T2), ['='], value(T3), {datatype(T1)}.

% display
stmt(display(T)) --> ['display'], value(T).

% assignment
stmt(assign(T1,T2)) --> id_name(T1), ['='], value(T2).
stmt(addAssign(T1,T2)) --> id_name(T1), ['+='], expr(T2).
stmt(subAssign(T1,T2)) --> id_name(T1), ['-='], expr(T2).
stmt(mulAssign(T1,T2)) --> id_name(T1), ['*='], expr(T2).
stmt(divAssign(T1,T2)) --> id_name(T1), ['/='], expr(T2).




% ternary if-else
stmt(ifelse(T1,T2,T3)) --> bool_expr(T1), ['?'], stmt(T2), [':'], stmt(T3).

% return statement
stmt(return(T)) --> ['return'], value(T).

%function call
stmt(call(T1,noneArg())) --> id_name(T1), ['(', ')'].
stmt(call(T1,T2)) --> id_name(T1), ['('] , arg_list(T2), [')'].
arg_list(T) --> value(T).
arg_list(argList(T1,T2)) --> value(T1), [','], arg_list(T2).


% if-else block
stmt_block(ifelse(T1,T2,T3)) --> ['if'], 
    ['('], bool_expr(T1), [')'], 
    ['{'], stmt_list(T2), ['}'],
    ['else'],
    ['{'], stmt_list(T3), ['}'].

% for-loop traditional
stmt_block(forT(T1,T2,T3,T4)) --> ['for-loop', '('], 
    stmt(T1), [';'], bool_expr(T2), [';'], stmt(T3), [')', '{'],
    stmt_list(T4), ['}'].

% for-loop range
stmt_block(forR(T1,T2,T3,T4)) --> ['for-loop', '('],
    id_name(T1), ['in', 'range', '('], expr(T2), [','], expr(T3), [')', ')', '{'],
    stmt_list(T4), ['}'].

% while-loop
stmt_block(while(T1,T2)) --> ['while', '('], bool_expr(T1), [')', '{'],
    stmt_list(T2), ['}'].

% FUNCTIONS
func_list(noneFunc()) --> [].
func_list(func(T1,T2,T3)) --> ['func'], id_name(T1), 
    ['('], parameter_list(T2), [')', '{'], 
    stmt_list(T3), ['}'].
func_list(funcList(func(T1,T2,T3),T4)) --> ['func'], id_name(T1), 
    ['('], parameter_list(T2), [')', '{'], 
    stmt_list(T3), ['}', ';'], func_list(T4).
% parameters
parameter_list(nonePmt()) --> [].
parameter_list(pmt(T1,T2)) --> [T1], id_name(T2), {datatype(T1)}.
parameter_list(pmtList(pmt(T1,T2),T3)) --> [T1], id_name(T2), {datatype(T1)}, [','], parameter_list(T3).



% program
program(prog(T1,T2)) --> func_list(T1), ['sup'], stmt_list(T2), ['peaceout'].

% Arithmetic test cases
test_arithmetic1 :-
    phrase(expr(ArithmeticExpr), ['10', '+', '5']),
    writeln('Arithmetic Expression-1:'),
    writeln(ArithmeticExpr).

test_arithmetic2 :-
    phrase(expr(ArithmeticExpr), ['15', '-', '7']),
    writeln('Arithmetic Expression-2:'),
    writeln(ArithmeticExpr).

test_arithmetic3 :-
    phrase(expr(ArithmeticExpr), ['4', '*', '3']),
    writeln('Arithmetic Expression-3:'),
    writeln(ArithmeticExpr).

test_arithmetic4 :-
    phrase(expr(ArithmeticExpr), ['8', '/', '2']),
    writeln('Arithmetic Expression-4:'),
    writeln(ArithmeticExpr).

test_arithmetic5 :-
    phrase(expr(ArithmeticExpr), ['25', '%', '7']),
    writeln('Arithmetic Expression-5:'),
    writeln(ArithmeticExpr).

% Boolean test cases
test_boolean1 :-
    phrase(bool_expr(BooleanExpr), ['Sahi', 'or', 'Galat']),
    writeln('Boolean Expression-1:'),
    writeln(BooleanExpr).

test_boolean2 :-
    phrase(bool_expr(BooleanExpr), ['not', 'Sahi', 'and', 'Galat']),
    writeln('Boolean Expression-2:'),
    writeln(BooleanExpr).

test_boolean3 :-
    phrase(bool_expr(BooleanExpr), ['10', '==', '5']),
    writeln('Boolean Expression-3:'),
    writeln(BooleanExpr).

test_boolean4 :-
    phrase(bool_expr(BooleanExpr), ['5', '>', '3']),
    writeln('Boolean Expression-4:'),
    writeln(BooleanExpr).

test_boolean5 :-
    phrase(bool_expr(BooleanExpr), ['x', '==', '10']),
    writeln('Boolean Expression-5:'),
    writeln(BooleanExpr).

% Statement test cases
test_statements1 :-
    phrase(stmt_list(Statements), ['int', 'x', ';', 'display', 'x', ';']),
    writeln('Statements-1:'),
    writeln(Statements).

test_statements2 :-
    phrase(stmt_list(Statements), ['int', 'x', '=', '5', ';', 'int', 'y', '=', 'x', '+', '3', ';']),
    writeln('Statements-2:'),
    writeln(Statements).

test_statements3 :-
    phrase(stmt_list(Statements), ['x', '==', '5', '?', 'display', 'Sahi', ':', 'display', 'Galat', ';']),
    writeln('Statements-3:'),
    writeln(Statements).

test_statements4 :-
    phrase(stmt_list(Statements), ['for-loop', '(', 'int', 'i', '=', '0', ';', 'i', '<', '5', ';', 'i', '+=', '1', ')', '{', 'display', 'i', ';', '}']),
    writeln('Statements-4:'),
    writeln(Statements).

test_statements5 :-
    phrase(stmt_list(Statements), ['while', '(', 'x', '>', '0', ')', '{', 'display', 'x', ';', 'x', '-=', '1', ';', '}']),
    writeln('Statements-5:'),
    writeln(Statements).


% Run all test cases
run_tests :-
    test_arithmetic1, test_arithmetic2, test_arithmetic3, test_arithmetic4, test_arithmetic5,
    test_boolean1, test_boolean2, test_boolean3, test_boolean4, test_boolean5,
    test_statements1, test_statements2, test_statements3, test_statements4, test_statements5.
