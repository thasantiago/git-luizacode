#Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a
#fórmula de Bhaskara.

a = float(input("Insira valor de a "))
b = float(input("Insira valor de b "))
c = float(input("Insira valor de c "))
delta = b**2 - (4*a*c)
x1 = (((-1)*b) + (delta**0.5)/(2*a))
x2 = (((-1)*b) - (delta**0.5)/(2*a))
if delta == 0:
    print("Raiz = ",x1)
elif delta > 0:
    print("Raiz 1 = ", x1, " Raiz 2 = ", x2) 
else:
    print(" Delta < 0 não existem raízes reais")