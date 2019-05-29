pesoPeixe = float (input("Informe a quantidade de peixes em KG: "))

if pesoPeixe > 50 :
 pesoExcedente = float (pesoPeixe - 50)
 multa = float (pesoExcedente * 4)
else: 
 multa = 0
 pesoExcedente = 0

print("Quantidade de peixe: ",pesoPeixe,"\nPeso excedente: ",round(pesoExcedente,2),
    "\nValor multa: ",round(multa,2))