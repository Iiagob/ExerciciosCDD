'''6. Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!'''
n1=int(input("Digite um valor: "))
if n1>10:
    print(f"O número {n1} é maior que 10!")
elif n1<10:
    print(f"O número {n1} é menor que 10")
else:
    print(f"O número é igual a {n1}!")