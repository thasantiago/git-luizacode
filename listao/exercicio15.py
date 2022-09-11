# Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
# o valor da conta de energia entre os moradores da casa. No programa eles informam o
#valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
# quanto cada um deverá contribuir com a conta de energia.

valor_da_conta = float(input("Informe o valor da conta de energia: "))
moradores = int(input("Informe quantos moradores irão dividir a conta: "))
valor_per_capita = valor_da_conta / moradores
print("Valor a pagar por pessoa = ", valor_per_capita)
