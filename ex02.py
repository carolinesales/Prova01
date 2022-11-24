print("Olá, Seja Bem-vindo(a) a Calculadora de IMC")

peso = float(input("Informe seu peso atual: "))
altura = float(input("Informe sua Altura: "))

#calculo do imc = (peso / altura²)
imc = peso / altura **2

print("O seu IMC é: {} ".format(imc))

if imc < 16:
    print("Magreza grave")

elif 16 and imc < 17:
    print("Magreza moderada")

elif 17 and imc < 18.5:
    print("Magreza leve")

elif 18.5 and imc < 25:
    print("Saudável")

elif 25 and imc < 30:
    print("Sobrepeso")

elif 30 and imc < 35:
    print("Obesidade Grau I")

elif 35 and imc < 40:
    print("Obesidade Grau II")

elif imc > 40:
    print("Obesidade Grau III")

