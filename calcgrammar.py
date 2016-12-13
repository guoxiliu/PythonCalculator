#
# This is a grammar definition file for the calclator.
#

from calctokens import *

# Grammar rules we will use in our calculator
grammar = [
    ('calc', ['element', 'calc']),
    ('calc', [ ]),
    ('element', ['FUNCTION', 'IDENTIFIER', 'LPAREN', 'optparams', 'RPAREN', 'compoundstmt']),
    ('element', ['sstmt']),
    ('optparams', ['params']),
    ('optparams', [ ]),
    ('params', ['IDENTIFIER', 'COMMA', 'params']),
    ('params', ['IDENTIFIER']),
    ('compoundstmt', ['LBRACE', 'stmts', 'RBRACE']),
    ('stmts', ['sstmt', 'stmts']),
    ('stmt_or_compound', ['sstmt']),
    ('stmt_or_compound', ['compoundstmt']),
    ('optsemi', [ ]),
    ('optsemi', ['SEMICOLON']),
    ('stmts', [ ]),
    ('sstmt', ['IF', 'exp', 'stmt_or_compound', 'optsemi']),
    ('sstmt', ['IF', 'exp', 'compoundstmt', 'ELSE', 'stmt_or_compound', 'optsemi']),
    ('sstmt', ['IDENTIFIER', 'EQUAL', 'exp', 'SEMICOLON']),
    ('sstmt', ['RETURN', 'exp', 'SEMICOLON']),
    ('sstmt', ['DEFINE', 'IDENTIFIER', 'EQUAL', 'exp', 'SEMICOLON']),
    ('sstmt', ['exp', 'SEMICOLON']),
    ('exp', ['IDENTIFIER']),
    ('exp', ['LPAREN', 'exp', 'RPAREN']),
    ('exp', ['NUMBER']),
    ('exp', ['STRING']),
    ('exp', ['TRUE']),
    ('exp', ['FALSE']),
    ('exp', ['NOT exp']),
    ('exp', ['exp', 'PLUS', 'exp']),
    ('exp', ['exp', 'MINUS', 'exp']),
    ('exp', ['exp', 'TIMES', 'exp']),
    ('exp', ['exp', 'DIVIDE', 'exp']),
    ('exp', ['exp', 'MOD', 'exp']),
    ('exp', ['exp', 'EQUEQU', 'exp']),
    ('exp', ['exp', 'LE', 'exp']),
    ('exp', ['exp', 'LT', 'exp']),
    ('exp', ['exp', 'GE', 'exp']),
    ('exp', ['exp', 'GT', 'exp']),
    ('exp', ['exp', 'ANDAND', 'exp']),
    ('exp', ['exp', 'OROR', 'exp']),
    ('exp', ['IDENTIFIER', 'LPAREN', 'optargs', 'RPAREN']),
    ('optargs', ['args']),
    ('optargs', [ ]),
    ('args', ['exp', 'COMMA', 'args']),
    ('args', ['exp']),
]


def addtochart(chart, index, state):
    if not state in chart[index]:
        chart[index] = chart[index] + [state]
        return True
    else:
        return False

def closure (grammar, i, x, ab, cd, j):
    next_states = []
    for r in [rule[1] for rule in grammar if cd <> [] and rule[0] == cd[0]]:
        next_states = next_states + [(cd[0], [], r, i)]
    return next_states

def shift (tokens, i, x, ab, cd, j):
    if cd <> [] and tokens[i][0] == cd[0]:
        return (x, ab+[cd[0]], cd[1:], j)
    else:
        return None

def reductions(chart, i, x, ab, cd, j):
    states = []
    if cd == []:
        for state in chart[j]:
            if state[2] <> [] and state[2][0] == x:
                states = states + [(state[0], state[1]+[x], state[2][1:], state[3])]
    return states

def parse(tokens, grammar):
    tokens = tokens + [("end_of_input_marker", "$")]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens)+1):
        chart[i] = []
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                # State === x -> ab.cd, j
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

                next_states = closure(grammar, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

                next_state = shift(tokens, i, x, ab, cd, j)
                if next_state <> None:
                    changes = addtochart(chart, i+1, next_state) or changes

                next_states = reductions(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

            if not changes:
                break
    for i in range(len(tokens)):
        print "== chart " + str(i)
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]
            print "    " + x + " ->",
            for sym in ab:
                print " " + sym,
            print " .",
            for sym in cd:
                print " " + sym,
            print " from " + str(j)
    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens)-1]



# Here are some test cases
case_1 = '''
    # Hello, here is our first test case!
    define x = 1 + 2;
    define y = true;
    define z = false;
'''
print '---------------output for test case 1---------------'
input_token_1 = test_lexer(case_1)
print input_token_1
result_1 = parse(input_token_1, grammar)
print result_1

case_2 = '''
    function max(a, b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
    max(4, 5);
'''
print '---------------output for test case 2---------------'
input_token_2 = test_lexer(case_2)
print input_token_2
result_2 = parse(input_token_2, grammar)
print result_2
