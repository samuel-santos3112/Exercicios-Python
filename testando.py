x=0
soma=0
while x < 4:
    notas = float (input("Informe notas: "))
    soma += notas
    x+=1
media = soma/4
print("%.2f" %media)