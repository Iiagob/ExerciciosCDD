'''15. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
while n1==n2:
    n2=int(input("Número inválido. Digite outro número:"))

if n1>n2:
    print(n1,n2)
else:
    print(n2,n1)