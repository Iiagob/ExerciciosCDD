'''16. Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte'''
i=int(input("Que horas o jogo começou: "))
f=int(input('Qual a hora que terminou o jogo: '))
if i<=f:
    duracao= f-i
else:
    duracao= 24-i+f
print(f"A duração do jogo foi de {duracao}h")