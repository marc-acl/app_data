import operator
import math

texto = "5"
texto2 = "3"
suma = "+"  
opr = "0"+"0"
print(float(texto)+float(opr)+float(texto2))
if opr == 0:
    print("Suma")

mem = []
mem.append(5)
mem.append(1)


print(mem)
print(len(mem))

txt = "/"
a = 10
b = 2
c = int(9.5)

print(c)

#division \\ se queda con la parte entera
print(math.fabs(2 - (3 // 4)))

buttons_list = ["0", ",", "=", "×", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "÷" ]
for idx, num in enumerate(buttons_list):
    row = math.fabs(2 - (idx // 4))
    column = math.fabs(0 + (idx % 4))
    print(row, column)