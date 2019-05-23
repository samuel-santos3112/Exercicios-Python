#!/usr/bin/python3 /home/samuel/Documentos/Python/ConversaoGraus
#coding: utf-8

grausFahrenheit = float (input("Informe a temperatura em graus Fahrenheit: "))

conversaoCelsius = float ((grausFahrenheit)-32) * (5/9)

print(grausFahrenheit,"graus Fahrenheit equivalem a",round(conversaoCelsius,2),"graus celsius")