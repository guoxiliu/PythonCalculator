
# This file contains only one function, optimize(exp), which takes an
# expression AST node and returns a new, simplified expression AST.
# In this file, we handle:
#
#       X * 1 == 1 * X == X     for all X
#       X * 0 == 0 * X == 0     for all X
#       X + 0 == 0 + X == X     for all X
#       X - X == 0              for all X
#
#       true && false == false
#       true && true == true
#       false && true == false
#       false && false == false
#
#       true || true == true
#       true || false == true
#       false || true == true
#       false || false == false
#
#       and constant folding for +, - and * (e.g., replace 1+2 with 3)
#

def optimize(exp):
    etype = exp[0]
    if etype == "binop":
        a = optimize(exp[1])
        op = exp[2]
        b = optimize(exp[3])

        # Arithmetic Laws
        if op == "*" and (a == ("number", 0) or b == ("number", 0)):
            return ("number", 0)
        elif op == "*" and a == ("number", 1):
            return b
        elif op == "*" and b == ("number", 1):
            return a
        elif op == "/" and a == ("number", 0):
            return ("number", 0)
        elif op == "/" and b == ("number", 1):
            return a
        elif op == "+" and a == ("number", 0):
            return b
        elif op == "+" and b == ("number", 0):
            return a
        elif op == "-" and (a == b):
            return ("number", 0)
        elif op == "-" and b == ("number", 0):
            return ("number", a)
        elif op == "^" and b == ("number", 0):
            return ("number", 1)

        # Constant Folding
        if a[0] == "number" and b[0] == "number":
            if op == "+":
                return ("number", a[1] + b[1])
            elif op == "-":
                return ("number", a[1] - b[1])
            elif op == "*":
                return ("number", a[1] * b[1])
            elif op == "/":
                return ("number", a[1] / b[1])
            elif op == "^":
                return ("number", a[1] ** b[1])

        # Boolean Laws
        if op == "&&" and (a == ("true", "true") and b == ("true", "true")):
            return ("true", "true")
        elif op == "&&" and (a == ("true", "true") and b == ("false", "false")):
            return ("false", "false")
        elif op == "&&" and (a == ("false", "false") and b == ("false", "false")):
            return ("false", "false")
        elif op == "&&" and (a == ("false", "false") and b == ("true", "true")):
            return ("false", "false")
        elif op == "||" and (a == ("false", "false") and b == ("false", "false")):
            return ("false", "false")
        elif op == "||" and (a == ("false", "false") and b == ("true", "true")):
            return ("true", "true")
        elif op == "||" and (a == ("true", "true") and b == ("true", "true")):
            return ("true", "true")
        elif op == "||" and (a == ("true", "true") and b == ("false", "false")):
            return ("false", "false")
        # If all else fails, return something good here ...
        return (etype, a, op, b)
    # leave this expression un-optimized
    return exp
