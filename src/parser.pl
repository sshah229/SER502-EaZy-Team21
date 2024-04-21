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



comparision(compareEquals(E1,E2))-->expression(E1),['=='],expression(E2),!.
comparision(compareGreaterEqual(E1,E2))-->expression(E1),['>='],expression(E2).
comparision(compareLesserEqual(E1,E2))-->expression(E1), ['<='],expression(E2).
comparision(compareGreater(E1,E2))-->expression(E1),['>'],expression(E2),!.
comparision(compareLesser(E1,E2))-->expression(E1),['<'],expression(E2),!.
comparision(compareNotEqual(E1,E2))-->expression(E1),['!='],expression(E2),!.

expression(expression('add'(T,E)))-->term(T),['+'],expression(E),!.
expression(expression('subtract'(T,E)))-->term(T),['-'],expression(E),!.
expression(expression('divide'(T,E)))-->term(T),['/'],expression(E),!.
expression(expression('multiply'(T,E)))-->term(T),['*'],expression(E),!.
expression(expression('modulo'(T,E)))-->term(T),['%'],expression(E),!.
expression(expression(T))-->term(T).
