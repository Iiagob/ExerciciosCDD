'''4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''
n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
n3=int(input("Digite um número: "))

if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)
