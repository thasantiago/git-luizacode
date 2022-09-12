#Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a
#venda for …
#● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
#● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da
#venda;
#● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
#● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
#● acima de R$50.000,00 a comissão será de 30% da venda.
#Faça um programa que informe o valor da comissão do vendedor para uma venda.

comissao = float(input("Insira valor da venda "))
if comissao >= 1000 and comissao <= 5000:
  print("Comissão = 10%")
elif comissao > 5000 and comissao <= 10000:
  print("Comissão = 20%")
elif comissao > 10000 and comissao <= 50000:
  print("Comissão = 25%")
elif comissao > 50000:   
  print("Comissão = 30%")
elif comissao < 1000:
  print("Sem comissão")  
  

  