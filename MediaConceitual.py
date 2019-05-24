#!/usr/bin/python3 /home/samuel/Documentos/Python/MediaConceitual.py
#coding: utf-8

nota1 = float(input("Informe nota 1: "))
nota2 = float(input("Informe nota 2: "))

media = float(nota1+nota2)/2

if media >9 and media <=10:
    conceito = 'A'
elif media > 7.5:
    conceito = 'B'
elif media > 6:
    conceito = 'C'
elif media > 4:
    conceito = 'D'
else :
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print("Aprovado!\nConceito:",conceito,"\nNota 1:",nota1,"\nNota 2:",nota2,"\nMedia:"
        ,round(media,2))
else:
    print("Reprovado!\nConceito:",conceito,"\nNota 1:",nota1,"\nNota 2:",nota2,"\nMedia:"
        ,round(media,2))