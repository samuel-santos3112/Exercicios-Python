idade = int(input ("Informe sua idade: "))
if idade >= 10 and idade < 20:
    print("Você é adolescente!")
elif idade >= 20 and idade < 30:
    print("Você é Jovem!")
elif idade >= 30 and idade < 40:
    print("Você é adulto!")
elif idade >=40 and idade <= 100:
    print("Você é idoso!")
else:
    print("Classificação não encontrada.")    
    