#
# This is a set of regular expressions defining a lexer for
# the calculator.
#

import ply.lex as lex

# Here are tokens that we will use in our calculator.
tokens = (
	'PLUS',			# +
	'MINUS',		# -
	'TIMES', 		# *
	'DIVIDE', 		# /
	'MOD',			# %
	'POWER', 		# ^
	'ANDAND',		# &&
	'OROR', 		# ||
	'EQUEQU', 		# ==
	'NOTEQU', 		# !=
	'NOT', 			# !
	'GE',			# >=
	'GT', 			# >
	'LE', 			# <=
	'LT', 			# <
	'EQUAL', 		# =
	'COMMA',		# ,
	'SEMICOLON',	# ;
	'LBRACE',		# {
	'RBRACE',		# }
	'LPAREN',		# (
	'RPAREN',		# )
	'IDENTIFIER',	# length_of_table
	'NUMBER',		# 123.456
	'DEFINE',		# define
	'FUNCTION',		# function
	'RETURN',		# return
	'WHILE',		# while
	'IF',			# if
	'ELSE',			# else
	'TRUE',			# true
	'FALSE',		# false
)

states = (
	('comment', 'exclusive'),
)

# Use regular expressions to build lexical analyzer
def t_comment(t):
	r'\#'							# Use #... to commment
	t.lexer.begin('comment')

def t_comment_end(t):
	r'\n'
	t.lexer.lineno += 1
	t.lexer.begin('INITIAL')
	pass

def t_comment_error(t):
	t.lexer.skip(1)

reversed = ['define', 'function', 'return', 'while', 'if', 'else', 'true', 'false']

t_PLUS 		= r'\+'
t_MINUS 	= r'-'
t_TIMES 	= r'\*'
t_DIVIDE 	= r'/'
t_MOD 		= r'%'
t_POWER		= r'\^'
t_ANDAND 	= r'&&'
t_OROR 		= r'\|\|'
t_EQUEQU	= r'=='
t_NOTEQU	= r'!='
t_NOT 		= r'!'
t_GE 		= r'>='
t_GT 		= r'>'
t_LE 		= r'<='
t_LT 		= r'<'
t_EQUAL 	= r'='
t_COMMA 	= r','
t_SEMICOLON = r';'
t_LPAREN 	= r'\('
t_RPAREN 	= r'\)'
t_LBRACE 	= r'{'
t_RBRACE 	= r'}'

t_ignore = ' \t\v\r'
t_comment_ignore = ' \t\v\r'

def t_newline(t):
	r'\n'
	t.lexer.lineno += 1

def t_error(t):
	print 'Illegal character: ' + t.value[0] + ' in line',
	print t.lineno
	t.lexer.skip(1)

# String tokens
def t_DEFINE(t):
	r'define'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_IF(t):
	r'if'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_TRUE(t):
	r'true'
	return t

def t_FALSE(t):
	r'false'
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z][A-Za-z_]*'
	return t

def t_NUMBER(t):
	r'-?[0-9]+(\.[0-9]*)?'
	t.value = float(t.value)
	return t
