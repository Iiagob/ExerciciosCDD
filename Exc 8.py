'''8. Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados'''
n=0
soma=0
for x in range(4):
    n = float(input("Digite um número: "))
    soma=soma+n
media= soma/4
print(media)