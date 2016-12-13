# Calculator
#
# This is the main function of our calculator.
#
import ply.lex as lex
import ply.yacc as yacc
import calctokens
import calcgrammar
import calcinterp

case_1 = '''
    function max(a, b){
        if (a > b){
            return a;
        } else{
            return b;
        }
    }
    out(max(3, 4));
'''

calclexer = lex.lex(module=calctokens)
calcparser = yacc.yacc(module=calcgrammar, tabmodule='parsetab')
ast = calcparser.parse(case_1, lexer=calclexer)
# print ast
print calcinterp.interpret(ast)