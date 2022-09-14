# Aplicando os conceitos de lista de compreensão com map, filter e reduce
from functools import reduce
lista = [100,248.90,88,124.90]

def desconto(preco):
  return preco * (1-0.1)

lista_com_desconto = map(desconto, lista)
print(list(lista_com_desconto))

menores_que_100 = filter( lambda e: e < 100, lista)
print(list(menores_que_100))

soma_elementos = reduce( lambda x, y: x+y, lista)
print(soma_elementos)