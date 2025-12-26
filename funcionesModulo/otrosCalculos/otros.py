import sympy

def matriz(a, b):
    x, y, z = sympy.symbols('x y z')
    return "Resultado matriz = " , sympy.linsolve(sympy.Matrix((a, b)), (x, y, z))
