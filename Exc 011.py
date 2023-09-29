'''11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''

ano=int(input("Qual sua idade?"))
meses= int(input("Quantos meses você tem? "))
dia= int(input("Quantos dias você tem? "))

diaano= ano*365
diames= meses*30

print(dia+diames+diaano)