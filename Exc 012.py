'''12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores'''
total= int(input("Digite o total de eleitores: "))
branco= int(input("Digite o total de votos brancos: "))
nulo= int(input("Digite o total de votos nulos: "))
valido= int(input("Digite o total de votos validos?: "))

totalbranco=(branco/total)*100
totalnulo=(nulo/total)*100
totalvalido=(valido/total)*100

print(f"A porcentagem de votos brancos é de {totalbranco}%,\nA porcentagem de votos nulos é {totalnulo}% \nA porcentagem de validos foi de {totalvalido}%")