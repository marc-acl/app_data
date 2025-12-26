import math
import sympy


def raiz(a):
    return "Raíz cuadrada de ", a, " es ", math.sqrt(a)


def integrar(a, b, c):
    x, y, z = sympy.symbols('x y z')  
    f = sympy.integrate((a*x**(b))**(c))/6
    return "Resultado integral = ", f