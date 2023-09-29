'''2. Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo'''

n1=int(input("Digite um número diferente de 0: "))

while n1==0:
    n1=int(input("<Número incorreto> Digite outro número:"))

if n1>0:
    print("Número positivo!")
else:
    print("Número negativo!")