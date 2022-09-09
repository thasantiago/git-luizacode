# Calcule a área de um quadrado com lado 2cm

from re import S


l = 2
quadrado = l * l
print('A área do quadrado é = ',quadrado)

# Uma mala custa R$120,00 , recebeu 5 % de desconto, quanto irá pagar?

mala = 120.00
desconto = 5
valor = ( mala * desconto ) / 100
valor_a_pagar = mala - valor
print(' Valor da mala com desconto = ',valor_a_pagar)

# Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
# será 200 Km. Quantas horas irá demorar a viagem.

deslocamento = 200
velocidade_media = 100
tempo = deslocamento / velocidade_media
print('A viagem irá demorar ', tempo ,' horas')

#João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
#sua média.

j = 2
m = 3
s = 1
total_pirulitos = j + m + s
media = total_pirulitos / 3
print('Total de pirulitos = ', total_pirulitos, ' / Média de pirulitos = ',media)

#Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
#verificação se a idade de Davi é maior que a idade de sua irmã.

davi = 13
irma = 7
if  davi > irma:
    eh_mais_velho = True
    print(eh_mais_velho)
else:
    print(False) 