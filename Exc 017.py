'''17.As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra.'''

maca=int(input("Digite a quantidade de maçãs compradas: "))
if maca>=12:
    v=maca*1
    print(f"O valor a pagar é de R${v}")
else:
    v=maca*1.3
    print(f"O valor da maçã é de R${v}")