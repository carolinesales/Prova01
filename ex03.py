par = 0
impar = 0


#numeros digitados pelo usuario

n1 = int(input("Informe um número Inteiro: "))
n2 = int(input("Informe um número Inteiro: "))
n3 = int(input("Informe um número Inteiro: "))
n4 = int(input("Informe um número Inteiro: "))
n5 = int(input("Informe um número Inteiro: "))
n6 = int(input("Informe um número Inteiro: "))
n7 = int(input("Informe um número Inteiro: "))
n8 = int(input("Informe um número Inteiro: "))
n9 = int(input("Informe um número Inteiro: "))
n10 = int(input("Informe um número Inteiro: "))

listaNumero = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

#verificar numeros pares e impares da lista digitada pelo usuario

for numero in listaNumero:
        if (numero % 2) == 0:
            print("O numero {} é par".format(numero))
        elif (numero % 2 != 0):
            print("O número {} é Impar".format(numero))



#maior e menor numero digitado
print("O maior numero digitado foi: {} ".format(max(listaNumero)))
print("O menor numero digitado foi: {} ".format(min(listaNumero)))