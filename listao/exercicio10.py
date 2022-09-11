# Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da
#pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar
#os dados coletados em linhas diferentes. E também, deverá informar quantos anos a
#pessoa terá no ano 2030.

nomeCompleto = input("Informe seu nome completo: ")
cidadeNasc = input("Informe sua cidade de nascimento: ")
anoNasc = int(input("Informe o ano de seu nascimento: "))
idade2030 = (2030 - anoNasc)
print(nomeCompleto)
print(cidadeNasc)
print(anoNasc)
print("Você terá ",idade2030,"anos em 2030")
