# Calculator
#
# This is the main function of our calculator.
#
import ply.lex as lex
import ply.yacc as yacc
import calctokens
import calcgrammar
import calcinterp
from functools import partial       # Handle input

global_env = (None, {"calculator output" : ""})

while True:
    prompt = partial(raw_input, ">>> ")				# Wait for user input
    stopword = ''			# Stop when encounter blank line
    content = ''			# Store user input
    for line in iter(prompt, stopword):
        content += line + '\n'

    calclexer = lex.lex(module=calctokens)
    # print "Lexical Analyzer:"
    # calclexer.input(content)
    # lexerout = []
    # while True:
    #     tok = calclexer.token()
    #     if not tok:
    #         break
    #     lexerout = lexerout + [(tok.type, tok.value)]
    # print lexerout

    calcparser = yacc.yacc(module=calcgrammar, tabmodule='parsetab')
    ast = calcparser.parse(content, lexer=calclexer)
    # print "Abstract Syntax Tree: "
    # print ast
    run_env = global_env
    run_env[1]["calculator output"] = ""	 # Clear last calculation result
    global_env = calcinterp.interpret(ast, run_env)
    print global_env[1]["calculator output"]

