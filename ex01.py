nome = input("Informe Seu Nome: ")
mes = int(input("Informe seu mês de nascimento: "))
ano = int(input("Informe seu ano de nascimento: "))

idadeAluno = ano - 2022

if idadeAluno <= 18 and mes <= 6:
    print("Pode Realizar a aula")

else:
    print("Poxa {}, infelizmente vamos ter que esperar mais um pouquinho".format(nome))
