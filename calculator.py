# Calculator
#
# This is the main function of our calculator.
#
import ply.lex as lex
import ply.yacc as yacc
import calctokens
import calcgrammar
import calcinterp

while True:
    stopword = ''
    content = ''
    for line in iter(raw_input, stopword):
        content += line + '\n'
    
    print content
    calclexer = lex.lex(module=calctokens)
    calcparser = yacc.yacc(module=calcgrammar, tabmodule='parsetab')
    ast = calcparser.parse(content, lexer=calclexer)
    # print ast
    print calcinterp.interpret(ast)
